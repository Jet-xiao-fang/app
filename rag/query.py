import sys

import config
from embedder import Embedder
from reranker import Reranker
from store import MilvusStore


def retrieve(query):
    embedder = Embedder()
    reranker = Reranker()
    store = MilvusStore()

    query_vector = embedder.encode_query(query)
    hits = store.search(query_vector, top_k=config.TOP_K)

    docs = []
    for hit in hits:
        entity = hit["entity"]
        docs.append({
            "text": entity["text"],
            "heading_path": entity["heading_path"],
            "similarity": hit["distance"],
        })

    if not docs:
        return []

    scores = reranker.rerank(query, [d["text"] for d in docs])
    for doc, score in zip(docs, scores):
        doc["score"] = score

    docs.sort(key=lambda d: d["score"], reverse=True)
    return docs[: config.RERANK_TOP_N]


def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("请输入问题: ")

    results = retrieve(query)
    print(f"\n问题: {query}\n")
    for i, r in enumerate(results, 1):
        print(f"[{i}] 标题路径: {r['heading_path']}")
        print(f"    重排分数: {r['score']:.4f} | 向量相似度: {r['similarity']:.4f}")
        print(f"    {r['text'][:200]}")
        print()


if __name__ == "__main__":
    main()
