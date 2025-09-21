import os
import json
from scripts.utils import load_model, read_json, save_numpy
import numpy as np
from sklearn.neighbors import NearestNeighbors


DATA_PATH = 'data/sample_jobs.json'
EMB_PATH = 'models/job_embeddings.npy'
META_PATH = 'models/job_meta.json'




def index_jobs():
	jobs = read_json(DATA_PATH)
	texts = [j['description'] + ' ' + j.get('title', '') for j in jobs]
	model = load_model()
	embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
	save_numpy(EMB_PATH, embeddings)

	os.makedirs(os.path.dirname(META_PATH), exist_ok=True)
	with open(META_PATH, 'w', encoding='utf-8') as f:
		json.dump(jobs, f, ensure_ascii=False, indent=2)

	# Optionally build sklearn index (not saved, just checks OK)
	nn = NearestNeighbors(n_neighbors=10, metric='cosine').fit(embeddings)

	print(f'Indexed {len(jobs)} jobs. Embeddings saved to {EMB_PATH}')




if __name__ == '__main__':
	index_jobs()