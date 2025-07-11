# lexi.sg-rag-backend-test






# 📚 Lexi RAG Backend Test

This is a backend service built using **FastAPI** that answers Indian legal queries using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant legal content from documents (PDF/DOCX), generates a response, and returns citation sources.

---

## 🚀 Hosted API

📎 Live Demo: [YOUR_DEPLOYED_URL_HERE]  
📷 Screenshots:  
- [ ] Upload your screenshots here  
- [ ] Test cases (valid, unrelated, empty, etc.)

---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Embeddings:** HuggingFace SentenceTransformers (`all-MiniLM-L6-v2`)  
- **Vector DB:** FAISS  
- **LLM:** DeepSeek via [Together API](https://www.together.ai/) (Open Source)  
- **PDF Loader:** LangChain (`PyMuPDFLoader` / `PDFMinerLoader`)  
- **Chunking:** `RecursiveCharacterTextSplitter`

---

## 📂 Project Structure


```
lexi.sg-rag-backend-test/
│
├── app/
│   ├── main.py                  # FastAPI app
│   ├── query\_LLM\_RESULT.py      # LLM & FAISS loader
│   ├── chunking.py              # PDF loader & chunker
│   ├── embedding.py             # FAISS indexer
│
├── data/
│   ├── RAW\_DATA/                # Original documents
│   ├── CHUNKS/                  # Chunked JSON
│   ├── FAISS/                   # FAISS index files
│
├── requirements.txt
├── README.md

```

---

## 🛠️ Setup Instructions

```bash
# Clone repository
git clone https://github.com/yourusername/lexi.sg-rag-backend-test.git
cd lexi.sg-rag-backend-test

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🔨 How to Run Locally

```bash
uvicorn app.main:app --reload
```

---

## 🔎 API Usage

### Endpoint: `POST /query`

**Request:**

```json
{
  "query": "Is an insurance company liable if the transport vehicle had no permit?"
}
```

**Response:**

```json
{
  "answer": "The insurance company is liable for third-party claims even if the transport vehicle lacked a permit, provided the policy covers third-party risks. ...",
  "citations": [
    {
      "text": "...the amount of Rs.1,737/- was paid towards third party premium...",
      "source": "DM Vs B Gangamma.pdf"
    },
    ...
  ]
}
```

---

## 📄 Sample Legal Documents

Store your input files in:

```
data/RAW_DATA/
```

Then run the following to generate chunked and embedded data:

```bash
python app/chunking.py
python app/embedding.py
```

FAISS index and chunked JSON will be created in:

* `data/CHUNKS/chunk_data.json`
* `data/FAISS/index.faiss`

---

## 🧪 Test Cases Covered

* ✅ Valid legal query
* ❌ Completely unrelated query
* ⚠️ Empty or junk input
* 🤔 Ambiguous phrasing

**Screenshots:**
📷 \[Insert test result screenshots here]

---

## ✅ Submission Checklist

* [x] `/query` route working
* [x] Chunked and embedded legal documents
* [x] Embedding using SentenceTransformers
* [x] Citation returned with answer
* [x] README with all instructions

---

## 👤 Author

**Mohamed Asif**
🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-asif-a5856817b/)
🐙 [GitHub](https://github.com/MohamedAsifS)

---

## 📝 Notes

* This project is aligned with Lexi’s backend assignment spec.
* Future plan: Use Indian legal corpus for citizen-accessible legal guidance tool "MyLaw".

```

Let me know when you're ready to host or need help preparing `requirements.txt`, `Procfile`, or anything else for Render/Replit.
```
