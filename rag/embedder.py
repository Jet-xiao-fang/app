import numpy as np

import config


class Embedder:
    def __init__(self, model_name=None, use_fp16=True):
        self.model_name = model_name or config.EMBEDDING_MODEL
        self._use_fp16 = use_fp16
        self._model = None

    @property
    def model(self):
        if self._model is None:
            from FlagEmbedding import BGEM3FlagModel
            self._model = BGEM3FlagModel(self.model_name, use_fp16=self._use_fp16)
        return self._model

    def encode(self, texts, batch_size=12):
        result = self.model.encode(
            list(texts),
            batch_size=batch_size,
            max_length=8192,
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False,
        )
        return np.asarray(result["dense_vecs"], dtype=np.float32)

    def encode_query(self, text):
        return self.encode([text])[0]
