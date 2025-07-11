import json
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

RAW_PDF=Path("../data/raw_pdf")
CHUNK=Path("../data/chunk")

text_split=RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=50,separators=["/n/n","/n"," ",""])
def load_and_split(pdf):
    """this function is intial step of RAG process where we get the pdf and split into chunks with help of langchain

    Args:
        pdf (_type_): PDF

    Returns:
        _type_: List[Document]
    """
    load=PyMuPDFLoader(pdf)
    pages=load.load()
    split=text_split.split_documents(pages)
    return split 

def get_chuck_to_json(data):
    """this functiuon change the list of chucks to JSON for permanenet store and reducing the chuck process for future need and for multi lang support

    Args:
        data (_type_): List
    """
    serializing_to_dict=[]
    for d in data:
        serializing_to_dict.append({
            "page_content":d.page_content,
            "metadata":d.metadata
        })
    
    path=CHUNK/"chunks.json"
    with open(path,"w",encoding="utf-8") as f:
        json.dump(serializing_to_dict,f,ensure_ascii=True,indent=2)

# now we get all the pdf from Data/raw_pdf folder with help of Path object where we can filter which type we need by using glob method
all_chunks=[]
for PDF in RAW_PDF.glob("*.pdf"):
    chunks=load_and_split(PDF) # we make it as chunks
    for chunk in chunks: #all chunk are Document Object 
        chunk.metadata["source"]=PDF.name # we set source for citation need
    all_chunks.extend(chunks)
        
    


# get_chuck_to_json(all_chunks)
