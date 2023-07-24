from fastapi import APIRouter, Request

from client_demo.helper.conversations import create_conversation
from client_demo.helper.utils import generate_chat_history

router = APIRouter(
    prefix='/backend',
    tags=['home'],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def backend(request: Request):
    data = await request.json()
    chat_history = generate_chat_history(data['chat_history'])
    response = create_conversation(data['query'], chat_history)
    return response, 200
