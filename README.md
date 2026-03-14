# 🧠 Agentic RAG System

Welcome to **Bhupesh's Agentic RAG** - An End-to-End Retrieval-Augmented Generation system. This project implements a fully functional AI-powered search and answering engine utilizing state-of-the-art Large Language Models (LLMs) and Vector Databases.

It features both a **Command Line Interface (CLI)** and a modern, beautifully designed **Streamlit Web Application** for interacting with the knowledge base.

## 🚀 Features

- **Agentic Workflow**: Utilizes LangGraph to build intelligent routing and execution loops.
- **Advanced Retrieval**: Uses FAISS for efficient, high-speed similarity search and vector storage.
- **Top-Tier Embeddings**: Powered by Voyage AI embeddings (`voyage-4-large` or equivalent).
- **Flexible LLM Support**: Designed to work with OpenAI or Sarvam LLMs.
- **Interactive UI**: A rich, dynamic Streamlit app with premium styling, responsive layout, and real-time response times.
- **Multiple Document Sources**: Capable of ingesting data from web URLs, local files, and more.

---

## 🛠️ Technology Stack

- **Frameworks:** [LangChain](https://python.langchain.com/), [LangGraph](https://python.langchain.com/docs/langgraph/)
- **UI:** [Streamlit](https://streamlit.io/)
- **Vector Store:** [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
- **Embeddings:** [Voyage AI](https://www.voyageai.com/)
- **Language Models:** OpenAI / Sarvam AI

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-rag-system.git
cd agentic-rag-system
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the root directory and add your necessary API keys. Example:

```env
OPENAI_API_KEY=your_openai_api_key
SARVAM_API_KEY=your_sarvam_api_key
VOYAGE_API_KEY=your_voyage_api_key
```

*(Note: Ensure you do not commit this file to GitHub!)*

---

## 🏃‍♂️ Usage

You can run the application in two different modes:

### 1. Streamlit Web Interface (Recommended)

Launch the interactive, beautifully designed web UI:

```bash
streamlit run streamlit_app.py
```

This will start a local web server (usually at `http://localhost:8501/`) where you can:
- Ask questions regarding the ingested documents
- See the source documents used to generate the answer limit
- View response times and search history

### 2. Command Line Interface (CLI)

For a quick terminal-based interaction:

```bash
python main.py
```

This script will initialize the system, run through some example questions, and optionally drop you into an interactive chat loop right in your terminal.

---

## 📁 Project Structure

```text
E2E Rag Project/
│
├── main.py                 # CLI application entry point
├── streamlit_app.py        # Streamlit web application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API Keys)
├── .gitignore              # Git ignored files
│
├── data/                   # Directory for storing input data files like urls.txt
├── src/                    # Source code directory
│   ├── config/             # Configuration modules
│   ├── document_ingestion/ # Document scraping, processing, and chunking
│   ├── vectorstore/        # FAISS vector store creation and management
│   └── graph_builder/      # LangGraph agent setup and execution logic
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/agentic-rag-system/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Bhupesh Danewa**
- Enthusiastic AI Engineer
- [LinkedIn](https://www.linkedin.com/in/bhupesh-danewa/)
- [GitHub](https://github.com/bhupeshdanewa07)

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
