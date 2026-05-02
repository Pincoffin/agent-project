import json

TOOL_FILE = "C:\\AI\\agent_v2\\tools\\registry.json"


def load_tools():
    try:
        with open(TOOL_FILE, "r") as f:
            return json.load(f)
    except:
        return {}