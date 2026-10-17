import os
import sys

import config
from chunker import markdown_to_chunks
from embedder import Embedder
from store import MilvusStore


def load_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "需求.md")
    text = load_markdown(path)

    chunks = markdown_to_chunks(text, max_chars=config.MAX_CHARS, overlap=config.OVERLAP)
    print(f"共切分出 {len(chunks)} 个块")

    store = MilvusStore()
    store.ensure_collection()

    embedder = Embedder()
    texts = [c["text"] for c in chunks]
    headings = [c["heading_path"] for c in chunks]

    batch = 32
    for i in range(0, len(chunks), batch):
        end = min(i + batch, len(chunks))
        vectors = embedder.encode(texts[i:end])
        store.insert(
            list(range(i, end)),
            texts[i:end],
            headings[i:end],
            vectors,
        )
        print(f"已写入 {end}/{len(chunks)}")

    print("入库完成")


if __name__ == "__main__":
    main()
