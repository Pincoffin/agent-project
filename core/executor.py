import os
import sys
import subprocess
import importlib.util

WORKSPACE = "C:\\AI\\agent_v2\\workspace"
TOOLS_DIR = os.path.join(WORKSPACE, "tools")


# ---------------- SAFE PATH RESOLVER ----------------

def resolve(path):
    if not path:
        return None

    # normalize slashes
    path = path.replace("\\", "/")

    # prevent accidental None crashes
    return os.path.join(WORKSPACE, *path.split("/"))


# ---------------- BUILT-IN TOOLS ----------------

def write_file(args):
    path = resolve(args.get("path") or args.get("filename"))
    content = args.get("content", "")

    if not path:
        return {"error": "missing path"}

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[WRITE] {path}")
    return {"status": "written", "path": path}


def run_script(args):
    path = resolve(args.get("path"))

    if not path:
        return {"error": "missing path"}

    try:
        if path.endswith(".py"):
            result = subprocess.run(
                [sys.executable, path],
                capture_output=True,
                text=True
            )
            print(result.stdout)
            return {"stdout": result.stdout, "stderr": result.stderr}

        elif path.endswith(".bat"):
            subprocess.Popen(path, shell=True)
            return {"status": "started"}

    except Exception as e:
        return {"error": str(e)}


def list_tools(_):
    files = os.listdir(TOOLS_DIR) if os.path.exists(TOOLS_DIR) else []
    print("[TOOLS]", files)
    return {"tools": files}


# ---------------- DYNAMIC TOOL LOADER ----------------

def run_dynamic_tool(tool_name, args):
    tool_path = os.path.join(TOOLS_DIR, f"{tool_name}.py")

    if not os.path.exists(tool_path):
        return {"error": f"tool not found: {tool_name}"}

    try:
        spec = importlib.util.spec_from_file_location(tool_name, tool_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        func = getattr(module, tool_name, None)

        if not func:
            return {"error": f"function {tool_name} not found in module"}

        return func(**args)

    except Exception as e:
        return {"error": str(e)}


# ---------------- ROUTER ----------------

def run_tool(action):
    tool = action.get("action")
    args = action.get("args", {}) or {}

    builtins = {
        "write_file": write_file,
        "run_script": run_script,
        "list_tools": list_tools
    }

    # 1. built-in tools
    if tool in builtins:
        return builtins[tool](args)

    # 2. dynamic tools
    return run_dynamic_tool(tool, args)