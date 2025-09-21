import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

EMB_PATH = 'models/job_embeddings.npy'
META_PATH = 'models/job_meta.json'
MODEL_NAME = 'all-MiniLM-L6-v2'


def load_index():
    if not os.path.exists(EMB_PATH) or not os.path.exists(META_PATH):
        raise FileNotFoundError('Index not found. Run scripts/index_jobs.py first to build embeddings.')
    embeddings = np.load(EMB_PATH)
    with open(META_PATH, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    return embeddings, meta


class Matcher:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.embeddings, self.meta = load_index()

    def match(self, resume_text, top_k=5):
        query_emb = self.model.encode([resume_text], convert_to_numpy=True)
        sims = cosine_similarity(query_emb, self.embeddings)[0]
        idx = sims.argsort()[::-1][:top_k]
        results = []
        for i in idx:
            r = self.meta[i].copy()
            r['score'] = float(sims[i])
            results.append(r)
        return results

