from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
from app.schema.material import MaterialBase, MaterialResponse
from app.service.material.material import MaterialService

router = APIRouter()
service = MaterialService()


# MODEL
@router.get("/")
async def root():
	return {'Hey Max - FastAPI - Python'}


# READ BY ID
@router.get("/find-material-by-id/{id}", status_code=200, response_model=MaterialResponse)
async def find_material_by_id(id: str):
    try:
        response = await service.find_material_by_id(id)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# READ
@router.get("/list-material", status_code=200, response_model=List[MaterialResponse])
async def list_material():
    try:
        response = await service.list_material()
        return response
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
	

# CREATE
@router.post("/create-material", status_code=201, response_model=MaterialResponse)
async def create_material(material: MaterialBase):
    try:
        response = await service.create_material(material)
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
 
# UPDATE
@router.patch("/update-material/{id}", response_model=MaterialBase)
async def update_material(id: str, material: MaterialBase):
    try:
        response = await service.update_material(id, material)
    
        if response.matched_count == 0:
            raise HTTPException(status_code=404, detail="Material not found")
        return response
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

 
# DELETE
@router.delete("/delete-material-by-id/{id}", response_model=Any)
async def delete_material_by_id(id):
    try:
        response = await service.delete_material_by_id(id)
        
        if not response:
            raise HTTPException(status_code=404, detail="Material não encontrado")
        
        return {
            "message": "deleted successfully",
            "data": response
        }
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
