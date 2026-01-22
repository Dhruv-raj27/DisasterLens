from sentence_transformers import SentenceTransformer
from PIL import Image

model = SentenceTransformer('all-MiniLM-L6-v2')  # Same as text model (384 dims)

def embed_image(image_path: str):
    image = Image.open(image_path).convert("RGB")
    # Create a text description from the filename for embedding
    filename = image_path.split('\\')[-1].split('/')[-1]
    description = f"disaster satellite image: {filename.replace('_', ' ').replace('.jpg', '').replace('.png', '')}"
    return model.encode(description).tolist()