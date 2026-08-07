import json
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct


client=QdrantClient(":memory:")

chunks=json.load(open(
    "embeddings/embeddings.json",
    encoding="utf-8"
))


client.create_collection(
    collection_name="lei_documents",
    vectors_config={
        "size":384,
        "distance":"Cosine"
    }
)


points=[]

for i,item in enumerate(chunks):
    points.append(
        PointStruct(
            id=i,
            vector=item["embedding"],
            payload={
                "content":item["content"],
                **item["metadata"]
            }
        )
    )


client.upsert(
    collection_name="lei_documents",
    points=points
)


print(
    f"Uploaded {len(points)} vectors"
)