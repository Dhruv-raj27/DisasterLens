from agent.search_agent import search_disaster_info
from agent.memory import show_memory

if __name__ == "__main__":
    search_disaster_info("flood disaster response")
    search_disaster_info("earthquake rescue operations")

    show_memory()
