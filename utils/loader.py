from langchain.document_loaders import PyPDFLoader, TextLoader, CSVLoader

def load_file(file_path):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".csv"):
        loader = CSVLoader(file_path)
    else:
        raise ValueError("Unsupported file format")
    return loader.load()
