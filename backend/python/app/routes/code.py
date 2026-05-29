from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from app.services.ollama_service import ollama_service
from app.utils.logger import logger

router = APIRouter()

class CodeGenerationRequest(BaseModel):
    prompt: str
    language: Optional[str] = "python"
    temperature: Optional[float] = 0.2

class CodeAnalysisRequest(BaseModel):
    code: str
    language: Optional[str] = "python"

class CodeResponse(BaseModel):
    code: str
    language: str
    explanation: str

@router.post("/generate", response_model=CodeResponse)
async def generate_code(request: CodeGenerationRequest):
    """Generate code based on prompt"""
    try:
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Prompt cannot be empty")
        
        # Check Ollama connection
        if not ollama_service.check_health():
            raise HTTPException(
                status_code=503,
                detail="Ollama service is not running"
            )
        
        # Create code generation prompt
        code_prompt = f"Generate {request.language} code for: {request.prompt}\n\nCode:"
        
        # Generate code
        code = ollama_service.generate(
            prompt=code_prompt,
            model=ollama_service.code_model,
            temperature=request.temperature
        )
        
        # Generate explanation
        explanation_prompt = f"Briefly explain this {request.language} code:\n{code}"
        explanation = ollama_service.generate(
            prompt=explanation_prompt,
            temperature=0.5
        )
        
        return CodeResponse(
            code=code,
            language=request.language,
            explanation=explanation
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating code: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze")
async def analyze_code(request: CodeAnalysisRequest):
    """Analyze code quality and provide suggestions"""
    try:
        if not request.code:
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        # Check Ollama connection
        if not ollama_service.check_health():
            raise HTTPException(status_code=503, detail="Ollama service is not running")
        
        # Create analysis prompt
        analysis_prompt = f"Analyze this {request.language} code and provide quality assessment, issues, and suggestions:\n{request.code}\n\nAnalysis:"
        
        # Get analysis
        analysis = ollama_service.generate(prompt=analysis_prompt, temperature=0.5)
        
        return {
            "analysis": analysis,
            "language": request.language
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing code: {e}")
        raise HTTPException(status_code=500, detail=str(e))
