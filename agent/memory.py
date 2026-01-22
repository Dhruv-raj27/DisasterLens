import json
import os
from datetime import datetime
from typing import List, Dict, Any

MEMORY_FILE = "session_memory.json"

def load_memory() -> List[Dict[str, Any]]:
    """Load existing memory from file"""
    if not os.path.exists(MEMORY_FILE):
        return []
    
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Error loading memory: {e}")
        return []

def save_to_memory(query: str, text_results: List, image_results: List):
    """Save query and results to memory"""
    memory = load_memory()
    
    interaction = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "text_results": [
            {
                "filename": r.payload['filename'],
                "score": float(r.score),
                "source": r.payload['source'],
                "event_type": r.payload['event_type']
            }
            for r in text_results
        ],
        "image_results": [
            {
                "filename": r.payload['filename'],
                "score": float(r.score),
                "source": r.payload['source'],
                "event_type": r.payload['event_type']
            }
            for r in image_results
        ],
        "total_results": len(text_results) + len(image_results)
    }
    
    memory.append(interaction)
    
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(memory, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Memory saved ({len(memory)} total interactions)")
    except Exception as e:
        print(f"⚠️  Error saving memory: {e}")

def show_memory():
    """Display all stored interactions"""
    memory = load_memory()
    
    if not memory:
        print("📭 No memory found")
        return
    
    print(f"\n🧠 MEMORY SUMMARY ({len(memory)} interactions)\n")
    print("=" * 70)
    
    for i, interaction in enumerate(memory, 1):
        print(f"\n{i}. Query: \"{interaction['query']}\"")
        print(f"   Time: {interaction['timestamp']}")
        print(f"   Results: {interaction['total_results']} items")
        print(f"   - Text: {len(interaction['text_results'])}")
        print(f"   - Images: {len(interaction['image_results'])}")
        
        if interaction['text_results']:
            top_text = interaction['text_results'][0]
            print(f"   Top match: {top_text['filename']} (score: {top_text['score']:.4f})")
    
    print("\n" + "=" * 70)

def clear_memory():
    """Clear all memory"""
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
        print("🗑️  Memory cleared")
    else:
        print("📭 No memory to clear")