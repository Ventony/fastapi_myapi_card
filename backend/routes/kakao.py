from fastapi import APIRouter
from backend.schemas.message import MessageDTO
from backend.services.service_kakao import KakaoService

router = APIRouter(
    tags=["kakao"],
)

@router.post("/")   # http://127.0.0.1:8000/kakao/ 를 의미함
async def send_message(msg: MessageDTO, db: Session = Depends(get_db)) -> dict:
    KakaoService().send_message(msg)
    return {"status": {"code": 200, "message": "success"}}


## 변경된 내용 잇음! 수정해야함