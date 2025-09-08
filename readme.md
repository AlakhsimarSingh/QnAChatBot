# ChatGroq RAG Bot

![App Screenshot](./Media/StreamliyUI.png)

A Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **Groq LLMs**, **FAISS**, and **Streamlit**.  
This bot loads documentation from the web, splits it into chunks, stores embeddings in FAISS, and answers user queries using **Groq’s `gemma2-9b-it` model**.

---

## Project Structure

groq/
└── app.py

requirements.txt

README.md
Media/
└── StreamliyUI.png
└── demo.mp4


---

## Features
- Uses **Groq LLMs** (`gemma2-9b-it`) for fast inference  
- Retrieval pipeline with **FAISS Vector Store**  
- Embeddings with **HuggingFace** (`all-MiniLM-L6-v2`)  
- Loads documents from a website (`WebBaseLoader`)  
- Simple Streamlit UI for chatting and inspecting retrieved docs  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/groq
2. Create and activate virtual environment
bash
Copy code
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the root directory (groq/) and add your Groq API key:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
▶ Running the App
bash
Copy code
streamlit run app.py
This will start a local Streamlit server. Open the URL (usually http://localhost:8501) in your browser.

## Usage
Enter your query in the text box (e.g., "What is LangSmith?")

The chatbot retrieves relevant documentation chunks from FAISS

Groq’s LLM (gemma2-9b-it) generates a context-aware response

Expand the Documents similarity search section to view retrieved sources

📦 Requirements
Your requirements.txt should contain:

txt
Copy code
langchain
langchain-community
langchain-core
langchain-groq
faiss-cpu
sentence-transformers
streamlit
python-dotenv
groq
⚠️ Notes
Default documents are loaded from LangSmith Docs.

You can modify WebBaseLoader in app.py to load any website or local files.

Switch embeddings (HuggingFace / Ollama) by uncommenting lines in app.py.

## Acknowledgements
LangChain

Groq

HuggingFace Sentence Transformers

Streamlit