from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.api import tools





app = FastAPI( title="Anargy API", description="Energy API for managing items and resources", version="1.0.0",tags=["Energy API"])



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tools.router)





