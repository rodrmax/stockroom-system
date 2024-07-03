from typing import Optional
from pydantic import BaseModel

# DTO
class MaterialBase(BaseModel):
    name: str
    model: str
    quantity: int
    
    
class MaterialResponse(BaseModel):
    id: str
    name: str
    model: str
    quantity: int
    create_at: str    