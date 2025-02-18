from typing import Optional

from langchain.embeddings import HuggingFaceEmbeddings

from embedchain.config import BaseEmbedderConfig
from embedchain.embedder.base_embedder import BaseEmbedder
from embedchain.models import EmbeddingFunctions


class HuggingFaceEmbedder(BaseEmbedder):
    def __init__(self, config: Optional[BaseEmbedderConfig] = None):
        super().__init__(config=config)

        embeddings = HuggingFaceEmbeddings(model_name=self.config.model)
        embedding_fn = BaseEmbedder._langchain_default_concept(embeddings)
        self.set_embedding_fn(embedding_fn=embedding_fn)

        vector_dimension = EmbeddingFunctions.HUGGING_FACE.value
        self.set_vector_dimension(vector_dimension=vector_dimension)
