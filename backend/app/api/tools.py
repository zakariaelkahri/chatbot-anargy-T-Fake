from fastapi import APIRouter 
import requests
from app.chatbot.agent import agent


router = APIRouter(prefix="/chatbot", tags=["Chatbot"])



@router.post("/agent")
def get_agent_response(query: str):
    """
    Get a response from the chatbot agent based on the provided query.
    """
    response = agent.invoke({"input": query})
    return {"response": response["output"]}

