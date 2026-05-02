import threading

from core.agent_core import loop, init_qdrant, set_task, inject_task

def start_agent():
    init_qdrant()
    loop()

def cli_loop():
    print("\nAgent CLI\n")

    while True:
        cmd = input("> ").strip()

        if cmd.startswith("task "):
            set_task(cmd[5:])
        elif cmd.startswith("inject "):
            inject_task(cmd[7:])
        elif cmd == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    threading.Thread(target=start_agent, daemon=True).start()
    cli_loop()