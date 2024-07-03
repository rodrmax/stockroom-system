from typing import List
from app.repository.material.material import MaterialRepository
from app.schema.material import MaterialBase, MaterialResponse


class MaterialService():
    def __init__(self):
        self.repository = MaterialRepository()
        
    async def find_material_by_id(self, id: str):
        return await self.repository.find_material_by_id(id)
    
    async def list_material(self):
        return await self.repository.list_material()
        
    async def create_material(self, material: MaterialBase):
        return await self.repository.create_material(material)
    
    async def update_material(self, id: str, material: MaterialBase):
        return await self.repository.update_material(id, material)
    
    async def delete_material_by_id(self, id: str):
        return await self.repository.delete_material_by_id(id)
    
    