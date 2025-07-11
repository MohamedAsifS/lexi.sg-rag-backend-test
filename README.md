# lexi.sg-rag-backend-test






# Lexi RAG Backend Test

This is a backend service built using **FastAPI** that answers Indian legal queries using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant legal content from documents (PDF/DOCX), generates a response, and returns citation sources.

---

## Hosted API

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

## 🧪 Test Cases Covered with **Screenshots:**

* ✅ Valid legal query
  <img width="1413" height="940" alt="image" src="https://github.com/user-attachments/assets/f2d2935e-3fa1-42c2-88f9-b4291234bd48" />

* ❌ Completely unrelated query
   <img width="1778" height="849" alt="image" src="https://github.com/user-attachments/assets/a825a821-6d5f-4976-9570-e2f70aae01a9" />

* ⚠️ Empty or junk input
  <img width="1428" height="823" alt="image" src="https://github.com/user-attachments/assets/aeeddc1f-fced-468b-9179-6ff00b840aaa" />
  <img width="1419" height="892" alt="image" src="https://github.com/user-attachments/assets/0fcc78f2-a254-4c9f-b9e6-f0f102f79212" />

* 🤔 Ambiguous phrasing
  <img width="1414" height="938" alt="image" src="https://github.com/user-attachments/assets/0b3a0d17-40bc-4186-95aa-6e31ab77a396" />
  




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


