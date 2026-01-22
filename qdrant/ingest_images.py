import os
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from embeddings.embed_image import embed_image

IMAGE_DATA_DIR = "data/images"

client = QdrantClient(url="http://localhost:6333")

def ingest_images():
    points = []
    point_id = 0

    if not os.path.exists(IMAGE_DATA_DIR):
        print(f"❌ Image directory not found: {IMAGE_DATA_DIR}")
        return

    for filename in os.listdir(IMAGE_DATA_DIR):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        filepath = os.path.join(IMAGE_DATA_DIR, filename)
        
        try:
            vector = embed_image(filepath)

            payload = {
                "source": "satellite_image",
                "filename": filename,
                "event_type": "disaster",
            }

            points.append(PointStruct(
                id=point_id,
                vector=vector,
                payload=payload
            ))
            point_id += 1
            print(f"✅ Processed: {filename}")
            
        except Exception as e:
            print(f"⚠️  Skipped {filename}: {str(e)}")
            continue

    if len(points) == 0:
        print("❌ No valid images found to ingest")
        return

    client.upsert(
        collection_name="disaster_images",
        points=points
    )

    print(f"✅ Ingested {len(points)} images")

if __name__ == "__main__":
    ingest_images()