from fastapi import APIRouter, HTTPException
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.utils.langchain_agent import get_langchain_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_input = request.messages[-1].content  # Get latest user message
    prev =[message.content for message in request.messages[:-1]]
    reply = get_langchain_response(user_input,prev)
    return ChatResponse(reply=reply)
