from sentence_transformers import SentenceTransformer
import numpy as np

# Loading the pre-trained sentence transformer
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    # Example of normal log 
    "Request from IP 192.168.1.5 performed a GET on path /assets/css/main.css and received status code 200.",
    # Example of suspecious log
    "Request from IP 10.0.5.12 performed a GET on path /products?id=1' OR '1'='1 and received status code 500."
]

print("Encoding sentences")
embeddings = model.encode(sentences)

print("Info about embeddings")
print(f"Shape of embeddings array: {embeddings.shape}")
print(f"Embedding for first sentence: {embeddings[0][::10]}")

np.save('log_embeddings.npy', embeddings)

