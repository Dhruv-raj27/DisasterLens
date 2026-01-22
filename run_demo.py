from agent.search_agent import search_disaster_info
from agent.memory import show_memory, clear_memory
import sys

def run_comprehensive_demo():
    """
    Comprehensive demo showcasing all system capabilities
    """
    
    print("\n" + "🌊 " * 35)
    print("        DISASTERLENS - MULTIMODAL DISASTER INFORMATION RETRIEVAL")
    print("🌊 " * 35 + "\n")
    
    print("=" * 70)
    print("SYSTEM OVERVIEW")
    print("=" * 70)
    print("✓ Multimodal semantic search (Text + Images)")
    print("✓ Persistent memory across queries")
    print("✓ Traceable reasoning with similarity scores")
    print("✓ 384-dimensional embedding space")
    print("✓ Qdrant vector database backend")
    print("=" * 70 + "\n")
    
    # Demo queries designed to show different capabilities
    demo_queries = [
        {
            "query": "flood affected regions and response",
            "purpose": "Text-heavy query (should retrieve flood reports strongly)"
        },
        {
            "query": "earthquake rescue operations",
            "purpose": "Different disaster type (should retrieve earthquake reports)"
        },
        {
            "query": "landslide disaster assessment",
            "purpose": "Image-focused query (should retrieve landslide imagery)"
        }
    ]
    
    for i, demo in enumerate(demo_queries, 1):
        print(f"\n{'=' * 70}")
        print(f"DEMO QUERY {i}/{len(demo_queries)}")
        print(f"Purpose: {demo['purpose']}")
        print(f"{'=' * 70}\n")
        
        search_disaster_info(demo['query'], limit=3)
        
        if i < len(demo_queries):
            input("\n⏸️  Press Enter to continue to next query...")
    
    # Show accumulated memory
    print("\n\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE - MEMORY SUMMARY")
    print("=" * 70)
    print("\nThe system has persisted all interactions in session_memory.json")
    print("This demonstrates long-term memory capability.\n")
    
    show_memory()
    
    # System stats
    print("\n" + "=" * 70)
    print("SYSTEM CAPABILITIES DEMONSTRATED")
    print("=" * 70)
    print("✅ Multimodal Retrieval - Text + Image results for each query")
    print("✅ Semantic Understanding - Ranked by similarity, not keywords")
    print("✅ Traceable Reasoning - Match quality + explanation for each result")
    print("✅ Persistent Memory - All queries saved with timestamps")
    print("✅ Cross-Modal Search - Images retrieved for text queries")
    print("=" * 70)
    
    print("\n📊 TECHNICAL DETAILS")
    print("   • Embedding Model: all-MiniLM-L6-v2 (384 dimensions)")
    print("   • Vector Database: Qdrant (HNSW indexing)")
    print("   • Distance Metric: Cosine similarity")
    print("   • Memory Format: JSON (session_memory.json)")
    print("=" * 70)
    
    print("\n🎯 NEXT STEPS")
    print("   • View memory: python view_memory.py")
    print("   • Interactive queries: python query_disaster.py")
    print("   • Add more data: Add files to data/text_reports/ or data/images/")
    print("   • Re-ingest: python -m qdrant.ingest_text && python -m qdrant.ingest_images")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--clear-memory":
        clear_memory()
        print("Memory cleared. Running fresh demo...\n")
    
    run_comprehensive_demo()