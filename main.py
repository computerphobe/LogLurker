from sentence_transformers import SentenceTransformer
import numpy as np

# Getting a embedding model.
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences =[

    "DELETE /usr/admin HTTP/1.0' 502 4963 '-' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4380.0 Safari/537.36 Edg/89.0.759.0' 45",
    "GET /usr/register HTTP/1.0' 502 5017 '-'' 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36' 1753"
]

embeddings = model.encode(sentences)
print(embeddings.shape)

similarity = model.similarity(embeddings, embeddings)
print(similarity)



