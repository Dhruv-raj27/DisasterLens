from agent.memory import show_memory, clear_memory
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--clear":
        clear_memory()
    else:
        show_memory()