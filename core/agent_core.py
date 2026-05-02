import time
import requests
import json
import uuid
import os
import re

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from core import executor
from core.planner import make_plan
from core.critic import evaluate_progress

# ---------------- CONFIG ----------------
CURRENT_TASK = None
PLAN = []
STEP_HISTORY = []
LAST_ACTION = None
LAST_ACTION_TYPE = None

OLLAMA_URL = "http://localhost:11434"
MODEL = "qwen:7b"

QDRANT_URL = "http://192.168.0.221:6333"
COLLECTION = "agent_memory"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- FILE HELPERS ----------------
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

SYSTEM = load_text(os.path.join(BASE_DIR, "..", "config", "system.txt"))
RULES = load_text(os.path.join(BASE_DIR, "..", "config", "rules.txt"))
PERSONALITY = load_text(os.path.join(BASE_DIR, "..", "config", "personality.txt"))
TOOLS = load_json(os.path.join(BASE_DIR, "..", "tools", "registry.json"))

# ---------------- QDRANT ----------------
client = QdrantClient(url=QDRANT_URL)

def init_qdrant():
    try:
        client.delete_collection(COLLECTION)
        print("[QDRANT] Old collection deleted")
    except:
        pass

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

    print("[QDRANT] Collection created (384 dim)")

# ---------------- EMBEDDING ----------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text):
    return embedder.encode(text).tolist()

# ---------------- MEMORY ----------------
def store_memory(text):
    vector = embed(text)

    client.upsert(
        collection_name=COLLECTION,
        points=[{
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {"text": text}
        }]
    )

def get_memory(query="recent actions"):
    vector = embed(query)

    result = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=5
    )

    hits = result.points

    if not hits:
        return "No memory."

    return "\n".join([h.payload.get("text", "") for h in hits])

# ---------------- LLM ----------------
def ask_llm(prompt):
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        data = r.json()
        return data.get("response", "")
    except Exception as e:
        print("[LLM ERROR]", e)
        return ""

# ---------------- PARSER ----------------
def extract_json(text):
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        obj = json.loads(text)
    except:
        matches = re.findall(r"\{.*\}", text, re.DOTALL)
        obj = None
        for m in matches:
            try:
                obj = json.loads(m)
                break
            except:
                continue

    if not obj:
        return None

    if "response" in obj:
        obj = obj["response"]

    if "command" in obj:
        obj["action"] = obj.pop("command")

    path = None
    content = None

    if "args" in obj:
        path = obj["args"].get("path")
        content = obj["args"].get("content")

    path = path or obj.get("file_path") or obj.get("path") or obj.get("script")

    if "file" in obj:
        path = obj["file"].get("name")
        content = obj["file"].get("content")

    if not content:
        content = obj.get("content")

    if path:
        path = path.replace("..\\workspace\\", "/projects/")
        path = path.replace("workspace/", "/projects/")
        path = path.replace("\\", "/")

        if not path.startswith("/projects/"):
            path = "/projects/" + os.path.basename(path)

    if content:
        return {
            "action": "write_file",
            "args": {"path": path, "content": content}
        }

    if obj.get("action") == "run_script" or "script" in obj:
        return {
            "action": "run_script",
            "args": {"path": path}
        }

    return None

# ---------------- TOOLS ----------------
def run_tool(data):
    tool = data.get("action")
    args = data.get("args", {})

    if tool == "write_file":
        executor.write_file(args)
    elif tool == "run_script":
        executor.run_script(args)
    elif tool == "list_tools":
        executor.list_tools(TOOLS)
    else:
        print("[INVALID TOOL]", tool)

# ---------------- CLI ----------------
def set_task(task):
    global CURRENT_TASK, PLAN, STEP_HISTORY
    CURRENT_TASK = task
    PLAN = make_plan()
    STEP_HISTORY.clear()
    print(f"[TASK] Set to: {task}")

def inject_task(text):
    global CURRENT_TASK
    CURRENT_TASK += f"\n{text}"

# ---------------- LOOP ----------------
def loop():
    global LAST_ACTION, LAST_ACTION_TYPE

    print("Agent running...\n")

    while True:
        if CURRENT_TASK is None:
            time.sleep(1)
            continue

        step = PLAN.pop(0) if PLAN else "Continue"

        prompt = f"""
TASK:
{CURRENT_TASK}

STEP:
{step}

RULES:
- Follow task exactly
- DO NOT invent tools
- Only use write_file or run_script
- After writing a file → MUST run it
- Never write twice in a row without running

Workspace:
{get_memory()}
"""

        reply = ask_llm(prompt)
        print("\n[RAW]\n", reply)

        data = extract_json(reply)
        if not data:
            print("[PARSE FAIL]")
            continue

        action_type = data.get("action")

        if action_type == "write_file" and LAST_ACTION_TYPE == "write_file":
            print("[FORCING EXECUTION]")
            data = {
                "action": "run_script",
                "args": {"path": "/projects/uptime_monitor.py"}
            }

        action_sig = str(data)
        if action_sig == LAST_ACTION:
            print("[LOOP BLOCKED]")
            continue

        LAST_ACTION = action_sig
        LAST_ACTION_TYPE = data.get("action")

        run_tool(data)

        store_memory(str(data))
        STEP_HISTORY.append(data)

        complete, next_step = evaluate_progress(data)
        if next_step:
            PLAN.insert(0, next_step)

        time.sleep(2)