import json

with open("chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)

sizes=[len(c["content"]) for c in chunks]

print("Total chunks:",len(chunks))
print("Average size:",sum(sizes)//len(sizes))
print("Largest chunk:",max(sizes))
print("Smallest chunk:",min(sizes))