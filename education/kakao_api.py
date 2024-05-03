# 카카오 API를 사용해서 나에게 톡 보내기
# 1. KAKAO Develpoer 설정
# 2. 인증 코드 요청 -> 카카오 서버 -> 인증 코드 전달 (인증 코드 = 1회성 -> 발급받음과 동시에 효력 X)
# 3. 인증 코드를 사용해서 토큰 발급
# 4. 토큰을 사용해서 나에게 메세지 보내기 



# 1. 카카오 OAUTH URL과 Redirect Key를 사용해서 인증 코드 요청
# - 웹 브라우저 URL: https://kauth.kakao.com/oauth/authorize?client_id=8e27c9db50b3a186482c7c863fc8040b&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message
# - 위의 코드를 웹 브라우저 URL에 입력하고 엔터 누르면 새로운 URL로 변경 -> code=[???]
# - [???] -> 카카오로부터 전달받은 인증코드

# 2. 인증코드를 사용해서 토큰 발급 받기

import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": "8e27c9db50b3a186482c7c863fc8040b",    #RESTAPI KEY
    "redirect_uri": "http://127.0.0.1:8000",
    "code": "_ADnSeq6jmVMCA-cnWp1pvpo75SuMnBDqnAVuO-LD_OycIX-31A8EWTWoxoKPXRoAAABjuT4YqIe0jm_MNo9Pw"
}

# 토큰 발급 코드
#response = requests.post(url, data= data)
#tokens = response.json()
#print(tokens)

#토큰 발급 이후 acess_token 작성

access_token = "4J0_Qj3uvNkV1wzS3DRldnGrF_8mf1ltEgUKPXQRAAABjuT4mpSt1856Xp2T3g"
msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + access_token
}

msg_data = {
    "template_object": json.dumps({
        "object_type": "text",
        "text": "카카오톡 테스트",
        "link": {"mobile_web_url": "https://www.naver.com"}
   })
}
response = requests.post(msg_url, headers=headers, data=msg_data)