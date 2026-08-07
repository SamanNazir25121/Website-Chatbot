import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_json(path):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)

def save_json(data,path):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

docs=load_json("metadata/documents.json")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=[]

for doc in docs:
    texts=splitter.split_text(doc["content"])

    for i,text in enumerate(texts):
        chunks.append({
            "content":text,
            "metadata":{
                **doc["metadata"],
                "chunk_id":i
            }
        })

save_json(chunks,"chunks/chunks.json")

print(f"Created {len(chunks)} chunks")