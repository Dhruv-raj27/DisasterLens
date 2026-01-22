from qdrant_client import QdrantClient
from embeddings.embed_text import embed_text
from agent.memory import save_to_memory
from agent.reasoning import explain_retrieval, format_reasoning_output

client = QdrantClient(url="http://localhost:6333")

def search_disaster_info(query: str, limit: int = 3, show_reasoning: bool = True):
    """
    Search for disaster information with full traceable reasoning
    
    Args:
        query: Search query
        limit: Max results per modality
        show_reasoning: Display detailed reasoning (default: True)
    """
    print(f"🔍 QUERY: {query}\n")
    print("=" * 70)
    
    query_vector = embed_text(query)
    
    # Search text reports
    text_results = client.query_points(
        collection_name="disaster_text",
        query=query_vector,
        limit=limit
    ).points
    
    print(f"\n📄 TEXT REPORT RESULTS ({len(text_results)} found):")
    print("=" * 70)
    
    for i, result in enumerate(text_results, 1):
        print(f"\n{i}. {result.payload['filename']}")
        
        if show_reasoning:
            reasoning = explain_retrieval(result, query, "TEXT")
            print(format_reasoning_output(reasoning))
        else:
            print(f"   └─ Score: {result.score:.4f}")
    
    # Search images
    image_results = client.query_points(
        collection_name="disaster_images",
        query=query_vector,
        limit=limit
    ).points
    
    print(f"\n🖼️  IMAGE RESULTS ({len(image_results)} found):")
    print("=" * 70)
    
    for i, result in enumerate(image_results, 1):
        print(f"\n{i}. {result.payload['filename']}")
        
        if show_reasoning:
            reasoning = explain_retrieval(result, query, "IMAGE")
            print(format_reasoning_output(reasoning))
        else:
            print(f"   └─ Score: {result.score:.4f}")
    
    # Summary
    print("\n" + "=" * 70)
    print(f"📊 SUMMARY:")
    print(f"   Total Results: {len(text_results) + len(image_results)}")
    print(f"   Text Documents: {len(text_results)}")
    print(f"   Images: {len(image_results)}")
    print(f"   Retrieval Method: Semantic vector search (384-dim embeddings)")
    print("=" * 70)
    
    # Save to memory
    save_to_memory(query, text_results, image_results)
    
    return {
        "text_results": text_results,
        "image_results": image_results
    }