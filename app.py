import streamlit as st
from langchain.llms import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from utils.loader import load_file
from utils.embedder import create_vector_store
from utils.retriever import hybrid_search
from utils.analytics import log_query, load_logs
from transformers import pipeline

st.set_page_config(page_title="Advanced RAG Chatbot", layout="wide")
st.title("🤖 Advanced Domain-Specific RAG Chatbot")

#file uploader
uploaded_files = st.file_uploader("Upload documents (PDF, TXT, CSV)", type=["pdf", "txt", "csv"], accept_multiple_files=True)

if uploaded_files:
    all_docs = []
    for uploaded_file in uploaded_files:
        path = f"data/{uploaded_file.name}"
        with open(path, "wb") as f:
            f.write(uploaded_file.read())
        all_docs.extend(load_file(path))

    db = create_vector_store(all_docs)
    #model
    model_name = "google/flan-t5-base" 
    pipe = pipeline("text2text-generation", model=model_name)
    
    #LLM
    llm = HuggingFacePipeline(pipeline=pipe)
    
    #summarizer
    summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizer = HuggingFacePipeline(pipeline=summarizer_model)

    chain = ConversationalRetrievalChain.from_llm(llm, retriever=db.as_retriever(), return_source_documents=True)

    query = st.text_input("Ask a question:")
    if query:
        result = chain({"question": query, "chat_history": []})
        answer = result["answer"]
        st.success(answer)

        log_query(query, answer)
        
        st.subheader("Summarization")
        text_to_summarize = st.text_area("Enter text (or paste document chunks) to summarize:")

        if st.button("Summarize"):
            if text_to_summarize:
                summary = summarizer_model(text_to_summarize, max_length=150, min_length=30, do_sample=False)
                st.success(summary[0]['summary_text'])
            else:
                st.warning("Please enter some text to summarize.")
    # dashboard
    with st.expander("📊 Analytics"):
        logs = load_logs()
        st.dataframe(logs.tail(10))
