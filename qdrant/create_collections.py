from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

# Connect to local Qdrant
client = QdrantClient(
    url="http://localhost:6333"
)

# -------- Text Collection --------
client.recreate_collection(
    collection_name="disaster_text",
    vectors_config=VectorParams(
        size=384,          # sentence-transformers dimension
        distance=Distance.COSINE
    )
)

# -------- Image Collection --------
client.recreate_collection(
    collection_name="disaster_images",
    vectors_config=VectorParams(
        size=512,          # CLIP image embedding size
        distance=Distance.COSINE
    )
)

print("✅ Qdrant collections created successfully")
