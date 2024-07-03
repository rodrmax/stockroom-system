from fastapi import FastAPI
from app.api.endpoints.material import material

app = FastAPI()

app.include_router(material.router, prefix="/api/v1/material", tags=["material"])
		

