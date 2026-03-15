"""Streamlit UI for Agentic RAG System - Simplified Version"""

import streamlit as st
from pathlib import Path
import sys
import time

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.config.config import Config
from src.document_ingestion.document_processor import DocumentProcessor
from src.vectorstore.vectorstore import VectorStore
from src.graph_builder.graph_builder import GraphBuilder

# Page configuration
st.set_page_config(
    page_title="Bhupesh's Agentic RAG",
    page_icon="🧠",
    layout="wide"
)

# Premium Custom CSS
st.markdown("""
    <style>
    /* Main theme styling */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Enhanced Main Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #6C63FF 0%, #3B3299 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(108, 99, 255, 0.4);
        color: white !important;
        border: none !important;
    }
    
    /* Profile Sidebar Styling */
    .profile-card {
        text-align: center;
        padding: 24px 16px;
        background: linear-gradient(180deg, rgba(108, 99, 255, 0.05) 0%, transparent 100%);
        border-radius: 16px;
        margin-bottom: 24px;
        border: 1px solid rgba(108, 99, 255, 0.1);
    }
    div a, div p, div h1, div h2, div h3 {
        color: inherit;
    }
    .profile-emoji {
        font-size: 64px;
        margin-bottom: 16px;
        line-height: 1;
    }
    .profile-name {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 6px;
        color: #e2e8f0;
    }
    .profile-title {
        font-size: 14px;
        color: #8c85ff;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Custom Header Styling */
    .hero-container {
        padding: 3rem 0 2rem 0;
        text-align: center;
        margin-bottom: 2rem;
        background: radial-gradient(circle at center, rgba(108, 99, 255, 0.05) 0%, transparent 70%);
        border-radius: 24px;
    }
    .main-header {
        font-size: 3.5rem !important;
        font-weight: 900;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 300% 300%;
        animation: gradient-animation 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 16px !important;
        letter-spacing: -1px;
        line-height: 1.2;
    }
    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    /* Global Footer Styling */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 12px;
        background: rgba(15, 23, 42, 0.85);        
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        font-size: 14px;
        font-weight: 500;
        z-index: 1000;
        color: #cbd5e1;
    }
    .heart {
        color: #FF6584;
        animation: pulse 1.5s infinite;
        display: inline-block;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    /* Adding bottom padding so footer doesn't hide content */
    .block-container {
        padding-bottom: 80px;
    }
    </style>
""", unsafe_allow_html=True)

def init_session_state():
    """Initialize session state variables"""
    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = None
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'history' not in st.session_state:
        st.session_state.history = []

@st.cache_resource
def initialize_rag():
    """Initialize the RAG system (cached)"""
    try:
        # Initialize components
        llm = Config.get_llm()
        doc_processor = DocumentProcessor(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        vector_store = VectorStore()
        
        # Use default URLs
        urls = Config.DEFAULT_URLS
        
        # Process documents
        documents = doc_processor.process_urls(urls)
        
        # Create vector store
        vector_store.create_vectorstore(documents)
        
        # Build graph
        graph_builder = GraphBuilder(
            retriever=vector_store.get_retriever(),
            llm=llm
        )
        graph_builder.build()
        
        return graph_builder, len(documents)
    except Exception as e:
        st.error(f"Failed to initialize: {str(e)}")
        return None, 0

def main():
    """Main application"""
    init_session_state()
    
    # Render Profile Sidebar
    with st.sidebar:
        st.markdown("""
            <div class="profile-card">
                <div class="profile-emoji">🚀</div>
                <div class="profile-name">Bhupesh Danewa</div>
                <div class="profile-title">Enthusiastic AI Engineer</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### About")
        st.info("Passionate about building intelligent systems, creating value, and pushing the boundaries of Agentic AI. Welcome to my intelligent search engine!")
        
        st.markdown("### Connect")
        st.markdown("🌐 [GitHub Profile](https://github.com/)\n\n"
                    "💼 [LinkedIn Connect](https://linkedin.com/)")
    
    # Title & Subtitle
    st.markdown("""
        <div class="hero-container">
            <h1 class="main-header">Bhupesh's Agentic RAG ✨</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Initialize system
    if not st.session_state.initialized:
        with st.spinner("Loading system..."):
            rag_system, num_chunks = initialize_rag()
            if rag_system:
                st.session_state.rag_system = rag_system
                st.session_state.initialized = True
                st.success(f"✅ System ready! ({num_chunks} document chunks loaded)")
    
    st.markdown("---")
    
    # Search interface
    with st.form("search_form"):
        question = st.text_input(
            "Enter your question:",
            placeholder="What would you like to know?"
        )
        submit = st.form_submit_button("🔍 Search")
    
    # Process search
    if submit and question:
        if st.session_state.rag_system:
            # 1. Show spinner while fetching the result
            with st.spinner("Searching the knowledge base..."):
                start_time = time.time()
                
                # Get answer
                result = st.session_state.rag_system.run(question)
                
                elapsed_time = time.time() - start_time
                
            # 2. Add to history outside spinner
            st.session_state.history.append({
                'question': question,
                'answer': result['answer'],
                'time': elapsed_time
            })
            
            # 3. Render the output independently of the spinner
            st.markdown("### 💡 Answer")
            st.success(result['answer'])
            
            # Show retrieved docs in expander outside spinner
            with st.expander("📄 Source Documents"):
                for i, doc in enumerate(result['retrieved_docs'], 1):
                    # Extract parent source (URL or file path) from metadata
                    source = doc.metadata.get("source", "Unknown source")
                    # For file paths, show just the file name; for URLs, show as-is
                    if source and not source.startswith("http"):
                        from pathlib import Path as _Path
                        source_display = _Path(source).name
                    else:
                        source_display = source

                    st.markdown(f"**📁 Source:** `{source_display}`")
                    st.text_area(
                        f"Document {i}",
                        doc.page_content[:300] + "...",
                        height=100,
                        disabled=True
                    )
            
            st.caption(f"⏱️ Response time: {elapsed_time:.2f} seconds")
    
    # Show history
    if st.session_state.history:
        st.markdown("---")
        st.markdown("### 📜 Recent Searches")
        
        for item in reversed(st.session_state.history[-3:]):  # Show last 3
            with st.container():
                st.markdown(f"**Q:** {item['question']}")
                st.markdown(f"**A:** {item['answer'][:200]}...")
                st.caption(f"Time: {item['time']:.2f}s")
                st.markdown("")

    # Global animated footer
    st.markdown("""
        <div class="footer">
            Made with <span class="heart">❤️</span> by <b>Bhupesh Danewa</b> | Driven by Curiosity & AI 🤖
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()