from fastapi import FastAPI 
from .RAG_Functions import query_LLM_RESULT

app=FastAPI()

@app.post("/query",status_code=200,tags=['Query'])
def query_and_response(request:str):
    return query_LLM_RESULT.Unload_FAISS_Find_Similiarity_return_result(request)
    