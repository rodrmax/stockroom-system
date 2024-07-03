import re
from bson import ObjectId

class Utils():
    def format_hash_id(obj_id):
        if isinstance(obj_id, ObjectId):
            obj_id = str(obj_id)
        elif not isinstance(obj_id, str):
            raise TypeError(f"Expected ObjectId or string, got {type(obj_id).__name__}")
        
        match = re.search(r"ObjectId\('([^']+)'\)", obj_id)
        if match:
            return match.group(1)
        return None