from backend.schemas.message import MessageDTO
import os
from dotenv import load_dotenv

class KakaoService:

    # 카카오 토큰 발급받기(+인증코드)
    def get_first_token(self):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "8e27c9db50b3a186482c7c863fc8040b",    #RESTAPI KEY
            "redirect_uri": "http://127.0.0.1:8000",
            "code": "_ADnSeq6jmVMCA-cnWp1pvpo75SuMnBDqnAVuO-LD_OycIX-31A8EWTWoxoKPXRoAAABjuT4YqIe0jm_MNo9Pw"
        }

    # Access Token 재발급(+Refresh Token)
    def refresh_access_token(self):
        pass

    # 나에게 카카오톡 보내기!
    def send_message(self, msg: MessageDTO):
        
        # 1. 토큰 유무 체크
        if os.path.isfile("./kakao_code.json"):
        #   - 토큰이 없는 경우 -> 토큰 발급
            tokens = self.refresh_access_token()
        #   - 토큰이 있는 경우 -> Refresh Token을 활용해서 재발급
        else:
            tokens = self.get_first_token()
        
        # 2. Access Token을 사용해서 나에게 카카오톡 보내기

        # 3. DB에 저장

        # + 스캐줄러 등록(Refresh Token 재발급)
        #   - Refresh Token은 유효기간 2달
        #   - 그리고 발급받은 날짜로부터 1달 후 재발급 가능
        #   - 케쥴러 -> 1달에 한번씩 Refresh Token을 재발급 받으세요!