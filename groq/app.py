from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from groq import Groq


import streamlit as st
import time
import os
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if "vectorstore" not in st.session_state:
    st.session_state.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.docs= st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("Chat Groq")
llm = ChatGroq(groq_api_key=groq_api_key, model="gemma2-9b-it")

prompt = ChatPromptTemplate.from_template(
    """Use the following pieces of context to answer the question at the end. 
<context>
{context}
</context>
Question: {input}
"""
)
document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
retriever = st.session_state.vectors.as_retriever()
retriver_chain = create_retrieval_chain(retriever, document_chain)
prompt = st.text_input("Ask a question about the Smith documentation")
if prompt:
    start = time.process_time()
    response = retriver_chain.invoke({"input":prompt})
    print("Respoonse time:", time.process_time() - start)
    st.write(response["answer"])

    with st.expander("Documents similarity search"):
        for i,d in enumerate(response["context"]):
            st.write(d.page_content)
            st.write("------------")