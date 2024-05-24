# DB와 커넥션 풀을 생성

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.common.config import Settings

SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# autocommit, autoflush -> False 사용 권장
# - commit 하면 Rollback 불가능!
# - flush는 트랜잭션 관련 기능...
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

function sendKakao(){
    type: "POST",
    contentType: "application.json; charset=UTF-8",
    dataType: "JSON",
    success: function(data) {
        document.querySelector("#kakao_form").reset()
        document.querySelector("#kakao_warp").style.display = "none";
        document.querySelector("#kakao_close_btn").style.display = "none";
        document.querySelector("kakao_btn").style.display = "flex";
    },
    error: function(data){
        console.log(data);
    }
    
}