from fastapi import APIRouter
from backend.schemas.message import MessageDTO
from backend.services.service_kakao import KakaoService

from fastapi import Depends
from backend.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["kakao"],
)

@router.post("/")   # http://127.0.0.1:8000/kakao/ 를 의미함
async def send_message(msg: MessageDTO, db: Session = Depends(get_db)) -> dict:
    KakaoService().send_message(msg)
    return {"status": {"code": 200, "message": "success"}}