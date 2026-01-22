from sentence_transformers import SentenceTransformer

# Load lightweight, fast model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """
    Converts text into a vector embedding
    """
    embedding = model.encode(text)
    return embedding.tolist()
