# Retrieval-Augmented Generation (RAG) Chatbot

An advanced **RAG-powered AI chatbot** that can answer questions from your uploaded documents (PDF, TXT, CSV) and also summarize text.  
Built using **LangChain, Hugging Face models, FAISS, and Streamlit**, it runs **completely free of cost** without requiring API keys.  

---

## Features
-  **Multi-document ingestion**: Upload PDFs, TXT, or CSV files.  
-  **Semantic + keyword hybrid search** with FAISS.  
-  **Conversational memory**: Handles multi-turn queries.  
-  **Summarization**: Summarize large documents with BART.  
-  **Analytics dashboard**: Logs queries and responses.  
-  **Deployable on Streamlit Cloud** for free.  

---

##  Tech Stack
- **LLMs**:  
  - [Flan-T5](https://huggingface.co/google/flan-t5-base) → Q&A  
  - [BART-Large-CNN](https://huggingface.co/facebook/bart-large-cnn) → Summarization  
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)  
- **Vector DB**: FAISS (local, free)  
- **Frameworks**: LangChain, Hugging Face Transformers  
- **UI**: Streamlit  

---

## Installation
```bash
git clone https://github.com/yourusername/rag-chatbot-advanced.git
cd rag-chatbot-advanced
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

---

##  Run the App
```bash
streamlit run app.py
```

---

##  Deployment (Streamlit Cloud)
- Push your repo to GitHub.

- Go to Streamlit Cloud → Create app.

- Point to app.py in your repo.

- Add requirements.txt.

- Deploy 
