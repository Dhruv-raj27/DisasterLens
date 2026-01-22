from agent.search_agent import search_disaster_info
from agent.memory import show_memory
import sys

def interactive_mode():
    """Interactive query mode"""
    print("\n" + "="*70)
    print("🌊 DISASTERLENS - Disaster Information Retrieval System")
    print("="*70)
    print("\nCommands:")
    print("  - Type your query to search")
    print("  - 'memory' to view past interactions")
    print("  - 'exit' to quit")
    print("="*70 + "\n")
    
    while True:
        try:
            query = input("\n💬 Enter query: ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            if query.lower() == 'memory':
                show_memory()
                continue
            
            print()
            search_disaster_info(query)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

def main():
    if len(sys.argv) > 1:
        # Command-line query
        query = " ".join(sys.argv[1:])
        search_disaster_info(query)
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()