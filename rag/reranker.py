import config


class Reranker:
    def __init__(self, model_name=None, use_fp16=True):
        self.model_name = model_name or config.RERANKER_MODEL
        self._use_fp16 = use_fp16
        self._model = None

    @property
    def model(self):
        if self._model is None:
            from FlagEmbedding import FlagReranker
            self._model = FlagReranker(self.model_name, use_fp16=self._use_fp16)
        return self._model

    def rerank(self, query, docs):
        pairs = [[query, d] for d in docs]
        scores = self.model.compute_score(pairs)
        if not isinstance(scores, list):
            scores = [scores]
        return [float(s) for s in scores]
