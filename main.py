import os
import streamlit as st
from streamlit_chat import message
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import tempfile

st.set_page_config(page_title="Smart Research Assistant", page_icon="🧠")

def load_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_file.read())
        path = temp.name
    loader = PyPDFLoader(path)
    return loader.load()

def create_vectorstore(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(chunks, embeddings)

def create_chain(vstore):
    llm = Ollama(model="phi")  # Or "mistral" if you have enough RAM
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=vstore.as_retriever(), memory=memory)

# === Streamlit App ===
st.title("📚 Smart Research Assistant")
uploaded_file = st.sidebar.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file:
    st.sidebar.success("PDF uploaded ✅")

    with st.spinner("Reading & indexing your document..."):
        docs = load_pdf(uploaded_file)
        vstore = create_vectorstore(docs)
        chain = create_chain(vstore)

    st.success("Document is ready! Ask me anything below 👇")

    if "history" not in st.session_state:
        st.session_state.history = []

    query = st.text_input("💬 Ask a question about the document")
    if query:
        result = chain({"question": query})
        st.session_state.history.append((query, result["answer"]))

    for i, (q, a) in enumerate(st.session_state.history):
        message(q, is_user=True, key=f"user_{i}")
        message(a, key=f"ai_{i}")
