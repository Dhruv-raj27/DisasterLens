# DisasterLens Quick Reference

## 🚀 Installation (5 minutes)

```bash
# 1. Clone & setup
git clone <repo-url>
cd disasterlens
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Qdrant
docker run -d -p 6333:6333 -p 6334:6334 qdrant/qdrant

# 4. Ingest data
python -m qdrant.ingest_text
python -m qdrant.ingest_images

# 5. Run demo
python run_demo.py
```

## 💻 Commands

| Command | Purpose |
|---------|---------|
| `python run_demo.py` | Run full demo (3 queries) |
| `python query_disaster.py` | Interactive query mode |
| `python query_disaster.py "flood"` | Single query from CLI |
| `python view_memory.py` | View query history |
| `python view_memory.py --clear` | Clear memory |

## 🔍 Sample Queries

- "flood affected regions and response"
- "earthquake rescue operations"
- "landslide disaster assessment"
- "hurricane evacuation procedures"
- "wildfire containment strategies"

## 📊 System Architecture

```
User Query → Text Embedding (384-dim) → Qdrant Vector Search
                    ↓
         [disaster_text] + [disaster_images]
                    ↓
         Similarity Ranking + Reasoning
                    ↓
         Results + Memory Save
```

## 🎯 Key Features

- ✅ **Multimodal:** Text + Image search
- ✅ **Memory:** Persistent query history
- ✅ **Reasoning:** Similarity scores + explanations
- ✅ **Fast:** <500ms query time
- ✅ **Scalable:** Vector database backend

## 🐛 Troubleshooting

**Qdrant not running?**
```bash
docker ps
docker start <container-id>
```

**Module not found?**
```bash
pip install -r requirements.txt
```

**Dimension mismatch?**
```bash
python -m qdrant.recreate_image_collection
python -m qdrant.ingest_images
```

## 📚 Documentation

- **README.md** - Full setup guide
- **REPORT.md** - Technical details
- **SUBMISSION_CHECKLIST.md** - Verification steps

## 🌐 Qdrant Dashboard

```
http://localhost:6333/dashboard
```

View collections, vectors, and search analytics.

---

**System Status:** Operational ✅  
**Version:** 1.0