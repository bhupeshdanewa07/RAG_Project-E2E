"""Configuration module for Agentic RAG system"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for RAG system"""
    
    # API Keys
    SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
    
    # Model Configuration
    LLM_MODEL = "sarvam-30b"
    
    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    
    # Default URLs
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]
    
    @classmethod
    def get_llm(cls):
        """Initialize and return the LLM model"""
        return ChatOpenAI(
            model=cls.LLM_MODEL,
            api_key=cls.SARVAM_API_KEY,
            base_url="https://api.sarvam.ai/v1"
        )