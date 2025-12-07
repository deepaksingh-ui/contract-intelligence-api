import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

class Retriever:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.corpus = []
        self.tfidf = None

    def index(self, chunks):
        self.corpus = chunks
        texts = [c['text'] for c in chunks]
        if texts:
            self.tfidf = self.vectorizer.fit_transform(texts)
        else:
            self.tfidf = None

    def query(self, q, top_k=3):
        if self.tfidf is None:
            return []
        q_vec = self.vectorizer.transform([q])
        scores = linear_kernel(q_vec, self.tfidf).flatten()
        top_idx = np.argsort(scores)[::-1][:top_k]
        results = []
        for i in top_idx:
            if scores[i] <= 0:
                continue
            c = self.corpus[i].copy()
            c['score'] = float(scores[i])
            results.append(c)
        return results
