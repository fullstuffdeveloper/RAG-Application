import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

vector = np.random.rand(1, dimension).astype('float32')
index.add(vector)

print("FAISS is working correctly!")