from pymilvus import MilvusClient, DataType

import config


class MilvusStore:
    def __init__(self, uri=None):
        self.uri = uri or config.MILVUS_URI
        self.collection_name = config.COLLECTION_NAME
        self.client = MilvusClient(uri=self.uri)

    def ensure_collection(self):
        if self.client.has_collection(self.collection_name):
            return
        schema = self.client.create_schema(auto_id=False, enable_dynamic_field=True)
        schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
        schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="heading_path", datatype=DataType.VARCHAR, max_length=4096)
        schema.add_field(
            field_name="dense_vector",
            datatype=DataType.FLOAT_VECTOR,
            dim=config.DENSE_DIM,
        )
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="dense_vector",
            index_type="HNSW",
            metric_type="COSINE",
            params={"M": 16, "efConstruction": 200},
        )
        self.client.create_collection(
            self.collection_name,
            schema=schema,
            index_params=index_params,
        )

    def insert(self, ids, texts, heading_paths, vectors):
        data = [
            {
                "id": i,
                "text": t,
                "heading_path": h,
                "dense_vector": v.tolist(),
            }
            for i, t, h, v in zip(ids, texts, heading_paths, vectors)
        ]
        self.client.insert(self.collection_name, data)

    def search(self, query_vector, top_k):
        res = self.client.search(
            collection_name=self.collection_name,
            data=[query_vector.tolist()],
            limit=top_k,
            output_fields=["text", "heading_path"],
            search_params={"metric_type": "COSINE", "params": {"ef": 128}},
        )
        return res[0] if res else []

    def drop(self):
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)
