import json
from langchain_huggingface import HuggingFaceEmbeddings


def load_json(path):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)


def save_json(data,path):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)


chunks=load_json(
    "chunks/chunks.json"
)


model=HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


embedded=[]

for chunk in chunks:

    vector=model.embed_query(
        chunk["content"]
    )

    embedded.append({
        "content":chunk["content"],
        "metadata":chunk["metadata"],
        "embedding":vector
    })


save_json(
    embedded,
    "embeddings/embeddings.json"
)


print(
    f"Created {len(embedded)} embeddings"
)