def get_memory():
    return "No memory yet."


def store_event(action, result):
    # later: store in Qdrant
    print("[MEMORY] stored:", action.get("action"))