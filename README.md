# lexi.sg-rag-backend-test






# 📚 Lexi RAG Backend Test

This is a backend service built using **FastAPI** that answers Indian legal queries using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant legal content from documents (PDF/DOCX), generates a response, and returns citation sources.

---

## 🚀 Hosted API

📎 Live Demo: [YOUR_DEPLOYED_URL_HERE]  
📷 Screenshot:  
<img width="1188" height="914" alt="msedge_K9o8MjXTwr" src="https://github.com/user-attachments/assets/f527ee4b-e63f-4be9-afb6-5fedc8c31053" />


---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Embeddings:** HuggingFace SentenceTransformers (`all-MiniLM-L6-v2`)  
- **Vector DB:** FAISS  
- **LLM:** DeepSeek via [Together API](https://www.together.ai/) (Open Source)  
- **PDF Loader:** LangChain (`PyMuPDFLoader` )  
- **Chunking:** `RecursiveCharacterTextSplitter`

---

## 📂 Project Structure


```
lexi.sg-rag-backend-test/src
│
├── RAG_Functions/
│   ├
│   ├── query_LLM_RESULT.py      # LLM & FAISS loader
│   ├── load_chunk.py             # PDF loader & chunker
│   ├── embedding.py             # FAISS indexer
│
├── data/
│   ├── RAW\_DATA/                # Original documents
│   ├── CHUNKS/                  # Chunked JSON
│   ├── FAISS/                   # FAISS index files
│── main.py                       # FastAPI app


```

---

## 🛠️ Setup Instructions

```bash

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Clone repository
git clone https://github.com/yourusername/lexi.sg-rag-backend-test.git
cd lexi.sg-rag-backend-test
# Install dependencies
pip install -r requirements.txt
````

---

## 🔨 How to Run Locally

```bash
uvicorn src.main:app --reload
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
<img width="1188" height="914" alt="msedge_K9o8MjXTwr" src="https://github.com/user-attachments/assets/bf47ec4b-ba98-4e3e-83c4-7f9a3e3d36f9" />


---



---

## 👤 Author

**Mohamed Asif**
🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-asif-a5856817b/)
🐙 [GitHub](https://github.com/MohamedAsifS)

---

## 📝 Notes

* This project is aligned with Lexi’s backend assignment spec.


```


