import datetime
from app.db.mongodb import Settings
from app.schema.material import MaterialBase, MaterialResponse
from app.utils.utils import Utils 
from bson import ObjectId
from typing import List

class MaterialRepository():
    def __init__(self):
        self.collection = Settings.database.material
        
    async def find_material_by_id(self, id: str):
        print(id)
        response = self.collection.find_one({"_id": ObjectId(id)})
        return {**response, "id": str(response["_id"])}
        
    async def list_material(self):
        materials = self.collection.find({})
        
        list_material: MaterialResponse = []
        for material in materials:
            material_dict = {**material, "id": str(material["_id"])}
            del material_dict["_id"]
            list_material.append(material_dict)
            
        response = list_material
        return response
        
    async def create_material(self, material: MaterialBase):
        document = material.model_dump()
        document['create_at'] = str(datetime.datetime.now())
        res = self.collection.insert_one(document)
        
        response = { "id": str(res.inserted_id), **document}
        return response   
    
    async def update_material(self, id: str, material: MaterialBase):
        document = material.model_dump()
        res = self.collection.find_one_and_update({"_id": ObjectId(id)},{"$set": document}, return_document=True)
        return res

    async def delete_material_by_id(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count > 0