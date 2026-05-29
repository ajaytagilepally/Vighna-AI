import requests
import json
from typing import Generator
from app.config import settings
from app.utils.logger import logger

class OllamaService:
    def __init__(self):
        self.host = settings.OLLAMA_HOST
        self.model = settings.OLLAMA_MODEL
        self.code_model = settings.OLLAMA_CODE_MODEL
        self.timeout = settings.OLLAMA_TIMEOUT
    
    def check_health(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.host}", timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Ollama health check failed: {e}")
            return False
    
    def generate(self, prompt: str, model: str = None, temperature: float = 0.7) -> str:
        """Generate text using Ollama"""
        model = model or self.model
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "stream": False
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json().get("response", "")
        except Exception as e:
            logger.error(f"Error generating text: {e}")
            raise
    
    def generate_stream(self, prompt: str, model: str = None, temperature: float = 0.7) -> Generator:
        """Generate text using Ollama with streaming"""
        model = model or self.model
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "stream": True
                },
                timeout=self.timeout,
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line)
                        yield data.get("response", "")
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            logger.error(f"Error in stream generation: {e}")
            raise
    
    def list_models(self) -> list:
        """List available models in Ollama"""
        try:
            response = requests.get(
                f"{self.host}/api/tags",
                timeout=5
            )
            response.raise_for_status()
            models = response.json().get("models", [])
            return [model["name"] for model in models]
        except Exception as e:
            logger.error(f"Error listing models: {e}")
            return []

# Create singleton instance
ollama_service = OllamaService()
