import together #I use togther freemium api which gives deepseek AI 
from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain.prompts import PromptTemplate 
from pathlib import Path
from environs import Env 
import os

env=Env()
env.read_env()

embed_model=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2") 

def chat_llm(prompt):
    result=together.Complete.create(
         prompt=prompt,
         model="deepseek-ai/DeepSeek-V3",
         max_tokens=256,
         temperature=0.7
    )
    
    return result 

prompt=PromptTemplate(
    input_variables=["context","query"],
    template="""
    Using the following legal context and use query, provide a clear response to the user's query and context in laymen term. Do not mention the word "context" or label the output as "Answer".
    and law is all about the Indian Law - so with context give correct result and if you can't find any relatvent add *** symbol in beging of a passage if you find just return the passage and don't need /n symbol
    Format the answer professionally. Start with a one-line legal conclusion. Then provide 2–3 concise, numbered reasoning points. Avoid repeating the same facts. Maintain legal tone.

    
    
    Context:
   {context}

   Question:
   {query}
"""

)

def content_gather(data):
    return "/n/n".join([d.page_content for d in data])

def final_resulting(data,context):
    if "***" in data['choices'][0]['text']:
        return {"answer":data['choices'][0]['text']}
    else:
        return {"answer":data['choices'][0]['text'],
            "citation":[
                {"text":d.page_content,"source":d.metadata["source"]} for d in context
            ]
            }


async def Unload_FAISS_Find_Similiarity_return_result(query):
    FAISS_PATH = os.path.abspath("src/data/FAISS")
    load=FAISS.load_local(FAISS_PATH,embeddings=embed_model,allow_dangerous_deserialization=True)
    similiar=load.similarity_search(query=query)
    
    context=content_gather(similiar)
    print(context)
    
    val=prompt.format(context=context,query=query)
    
    Actual_result=chat_llm(val)
    
    
    return final_resulting(Actual_result,similiar)

# final=Unload_FAISS_Find_Similiarity_return_result("Is an insurance company liable to pay compensation if a transport vehicle involved in an accident was being used without a valid permit?")
# print(final)