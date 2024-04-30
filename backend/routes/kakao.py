from fastapi import APIRouter

router = APIRouter(
    tags=["kakao"],
)

@router.post("/")   # http://127.0.0.1:8000/kakao/ 를 의미함
async def send_message(msg: MessageDTO) -> dict:            
    return {"status": {"code": 200, "message": "success"}}