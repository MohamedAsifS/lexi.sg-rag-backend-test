import json
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS 
from transformers import AutoTokenizer 
from langchain.schema import Document

embed_model=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
json_path=Path("../data/chunk/chunks.json")

def token_maker(data):
    """get paramter of page_content data from json and get token for each chunkin list of token where its ensures the token length dosn't exceed than model acceptance

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    token=AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    return [token.encode(d) for d in data]

def token_and_change_to_document(path):
    """this function takes json path which we make JSOn in Intial step and we change data to document and add token size and actual token

    Args:
        path (_type_): Path

    Returns:
        _type_: list[Document]
    """
    
    
    with open(path,"r",encoding="utf-8") as f:
        data=json.load(f)
    document_changer=[Document(page_content=d["page_content"],metadata=d["metadata"])   for d in data]
    content_for_token=[d.page_content  for d in document_changer]
    tokens=token_maker(content_for_token)
    
    for token,data in zip(tokens,document_changer):
        data.metadata["token_count"]=len(token)
        data.metadata["token"]=token 
    return document_changer

def embbed_and_store_to_faiss(document:list[Document]):
    text=[d.page_content for d in document]
    metadata=[d.metadata  for d in document]
    embed=FAISS.from_texts(texts=text,embedding=embed_model,metadatas=metadata)
    embed.save_local("../data/FAISS")
    print("Stored as FAISS")

embbed_and_store_to_faiss(token_and_change_to_document(json_path))