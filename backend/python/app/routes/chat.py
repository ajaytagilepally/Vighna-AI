from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from app.services.ollama_service import ollama_service
from app.utils.logger import logger

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = None
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    model: str
    temperature: float

@router.post("/send", response_model=ChatResponse)
async def send_message(request: ChatRequest):
    """Send a message and get AI response"""
    try:
        if not request.message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Check Ollama connection
        if not ollama_service.check_health():
            raise HTTPException(
                status_code=503,
                detail="Ollama service is not running. Please start Ollama."
            )
        
        # Generate response
        response = ollama_service.generate(
            prompt=request.message,
            model=request.model,
            temperature=request.temperature
        )
        
        return ChatResponse(
            response=response,
            model=request.model or ollama_service.model,
            temperature=request.temperature
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_models():
    """Get available models"""
    try:
        models = ollama_service.list_models()
        return {"models": models}
    except Exception as e:
        logger.error(f"Error getting models: {e}")
        raise HTTPException(status_code=500, detail=str(e))
