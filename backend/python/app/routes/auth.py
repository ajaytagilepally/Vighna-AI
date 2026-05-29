from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class AuthResponse(BaseModel):
    user_id: str
    username: str
    token: str
    token_type: str = "bearer"

# Temporary in-memory user storage (replace with database)
users_db = {}

@router.post("/register", response_model=AuthResponse)
async def register(request: RegisterRequest):
    """Register a new user"""
    try:
        if request.username in users_db:
            raise HTTPException(status_code=400, detail="User already exists")
        
        user_id = str(uuid.uuid4())
        users_db[request.username] = {
            "user_id": user_id,
            "username": request.username,
            "email": request.email,
            "password": request.password,
            "created_at": datetime.now()
        }
        
        return AuthResponse(
            user_id=user_id,
            username=request.username,
            token=user_id
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest):
    """Login a user"""
    try:
        if request.username not in users_db:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        user = users_db[request.username]
        if user["password"] != request.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return AuthResponse(
            user_id=user["user_id"],
            username=user["username"],
            token=user["user_id"]
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
