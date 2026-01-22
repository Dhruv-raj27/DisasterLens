import os
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from embeddings.embed_text import embed_text

TEXT_DATA_DIR = "data/text_reports"

client = QdrantClient(url="http://localhost:6333")

def ingest_text_files():
    points = []

    for idx, filename in enumerate(os.listdir(TEXT_DATA_DIR)):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(TEXT_DATA_DIR, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        vector = embed_text(content)

        payload = {
            "source": "text_report",
            "filename": filename,
            "event_type": "disaster",
        }

        points.append(PointStruct(
            id=idx,
            vector=vector,
            payload=payload
        ))

    client.upsert(
        collection_name="disaster_text",
        points=points
    )

    print(f"✅ Ingested {len(points)} text reports")

if __name__ == "__main__":
    ingest_text_files()