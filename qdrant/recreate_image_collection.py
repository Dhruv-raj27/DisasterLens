from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

# Delete the old collection
try:
    client.delete_collection(collection_name="disaster_images")
    print("✅ Deleted old disaster_images collection")
except Exception as e:
    print(f"Collection doesn't exist or error: {e}")

# Create new collection with correct dimensions (384)
client.create_collection(
    collection_name="disaster_images",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)
print("✅ Created new disaster_images collection with 384 dimensions")