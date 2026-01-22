from typing import Dict, Any

def explain_retrieval(result: Any, query: str, modality: str) -> Dict[str, str]:
    """
    Generate detailed reasoning for why a result was retrieved
    """
    score = result.score
    filename = result.payload['filename']
    event_type = result.payload['event_type']
    
    # Determine match quality
    if score > 0.6:
        match_quality = "STRONG"
        explanation = f"High semantic similarity ({score:.4f}) indicates this {modality.lower()} is highly relevant"
    elif score > 0.4:
        match_quality = "MODERATE"
        explanation = f"Moderate semantic similarity ({score:.4f}) suggests partial relevance"
    else:
        match_quality = "WEAK"
        explanation = f"Lower similarity ({score:.4f}) but still potentially relevant"
    
    reasoning = {
        "match_quality": match_quality,
        "score": f"{score:.4f}",
        "modality": modality,
        "event_type": event_type,
        "explanation": explanation,
        "metadata_match": f"Event type '{event_type}' indexed",
        "retrieval_method": "Vector similarity search using semantic embeddings"
    }
    
    return reasoning

def format_reasoning_output(reasoning: Dict[str, str]) -> str:
    """
    Format reasoning as a readable output
    """
    output = []
    output.append(f"   ├─ Match Quality: {reasoning['match_quality']}")
    output.append(f"   ├─ Similarity Score: {reasoning['score']}")
    output.append(f"   ├─ Modality: {reasoning['modality']}")
    output.append(f"   ├─ Event Type: {reasoning['event_type']}")
    output.append(f"   ├─ Explanation: {reasoning['explanation']}")
    output.append(f"   ├─ Metadata: {reasoning['metadata_match']}")
    output.append(f"   └─ Method: {reasoning['retrieval_method']}")
    
    return "\n".join(output)