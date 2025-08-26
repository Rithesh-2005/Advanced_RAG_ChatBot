import re

def hybrid_search(query, db, docs):
    """vector search + keyword match"""
    results = db.similarity_search(query, k=3)
    keyword_hits = [doc for doc in docs if re.search(query, doc.page_content, re.IGNORECASE)]
    return results + keyword_hits
