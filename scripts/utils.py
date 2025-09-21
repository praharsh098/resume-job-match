import os
import json
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = 'all-MiniLM-L6-v2'

def load_model():
    return SentenceTransformer(MODEL_NAME)

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_numpy(path, arr):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path, arr)

def load_numpy(path):
    return np.load(path)


