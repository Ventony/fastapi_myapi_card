# fastapi_myapi_card
fastapi, jinja2, sqlalchemy, mariadb, docker, docker-compose, aws, langchain, apscheduler, uvicorn, requests

# pip command
＞ pip install -r requirements.txt → requirements.txt에 있는 pip 전부 설치
＞ pip freeze > requirements.txt → 현재 설치되어있는 pip 전부를 requirements.txt에 표시

# 라이브러리 설명
1. fastapi: 웹 프레임워크 + API
2. uvicorn: WAS(웹 어플리케이션 서버)
3. jinja2: 템플릿 엔진(HTML, CSS, JS)

## Web 프로그래밍 기초 설명
#### 1. URL
    - http://127.0.0.1:8000 = http://localhost:8000
    - 127.0.0.1 과 localhost는 루프백 주소(현재 디바이스의 IP)
    - http → 웹 프로토콜
    - 8000 → Port
    - http 프로토콜에서 제공하는 함수 (get, post, put, delete)
    - http://127.0.0.1:8000/ooooo → 쿼리스트링 (get 방식)
    - http://127.0.0.1:8000/member?id=abc1234&name=cherry → member에 ? 뒤 값을 전달 & == AND
    - 숨겨야하는 정보들 (post 방식)

#### 2. DAO and DTO(VO)
    - DAO(Data Access Object): CRUD (Create, Read, Update, Delete) 할 때 사용
       + Create: INSERT
       + Read:   SELETE
       + Update: UPDATE
       + Delete: DELETE

    - DTO(Data Transfer Object): 데이터를 전달할 때 사용
    
#### 3. 유효성(Validation) 체크
  - 유효성체크는 사용자의 값이 올바른 값인지 체크
     + 예: 이메일(이메일 형식인지?)
  - 역사
    1. 유효성체크: 서버 → 과부하
    2.            클라이언트(웹브라우저) → JS (현재도 사용중)
    3.            서버 추가 → 더블 체크(pydantic)
    
#### 4. 웹 동작 과정 Process
  - 정의: Client (=Web browser), Server (= 회사)
  - 동작: Client → request → Server → response → Client
  - 동작(심화): View단(Client) → Controller단(main, router) → Service단 → Model단(DB)
    + View단: 사용자에게 보여지는 화면
    + Controll단: 사용자가 요청한 URL과 데이터(유효성 체크)를 전달받고 일을 분배하는 곳
    + Service단: 실제 기능구현
    + Model단: DB관련된 기능 구현 (DAO: Databass Access Object)
    1. Client 에서 form 또는 ajax 등을 사용해서 request(+data) #fnc.js의 $.ajax
      - URL: http://127.0.0.1:8000/kakao/
      - method: POST
      - data: json
    2. Server의 main.py에서 요청 받기 → 해당 라우터로 전달
    3. Server의 해당 Router(Kakao)에서 요청과 데이터를 받음
      - pydantic을 활용한 data validation check (유효성 검증) → Data
    4. Server의 Service단으로 request와 data를 전달


## 카카오 나에게 톡 보내기
- 인증코드 URL(Base) : https://kauth.kakao.com/oauth/authorize?client_id={REST API 키}&redirect_uri={Redirect URI}&response_type=code&scope=talk_message
- 인증코드 URL(Mine) : https://kauth.kakao.com/oauth/authorize?client_id=8e27c9db50b3a186482c7c863fc8040b&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message


#### 1. 카카오 API 용어
- 인증코드: 1회성, 토큰(Access, Refresh) 발급 받기 위해 사용!
- Access 토큰: 카카오 API 서비스를 이용할 때 사용
- Refresh 토큰: Access 토큰을 재발급 받기 위해 사용
- 생명주기: 인증코드(1회), Access(6시간), Refresh(2달)
- *Refresh 토큰은 발급받고 1달 후 부터 재발급 가능
- Access와 Refresh 재발급 받는 코드는 동일
- └ 재발급 코드: Refresh 발급받은지 1달 미만, Access 토큰만 재발급해서 리턴
- └ 재발급 코드: Refresh 발급받은지 1달 이상, Access 토큰과 Refresh 토큰 재발급해서 리턴

#### 2. 카카오 API 사용 방법
1. kakao Developer 사이트에서 "권한 허용 및 동의"
2. 웹 브라우저 URL을 통해 인증 코드 발급
3. 인증코드 사용해서 토큰(Access, Refresh) 발급
4. Access 사용해서 서비스 이용!
5. +1달에 한번씩 Refresh 토큰 재발급 스케줄링

### #. 각종 이야기
- 원래 js는 정적인 동작 (static) → 서버를 타지 않고 클라이언트에서 작동
- 동적인 동작 (Dynamic) → node.js  탄생으로 동적 js가 가능해짐

1. Spring (JAVA)
2. Node (JS)
3. Django, flask, fastapi (PYTHON)

- 전자정부 프레임워크 → 정부에서 만든 프레임 워크 (정부 관련 사업 진행시 사용하는 툴)
- → Spring (JAVA)를 기반으로 만듬
- → 웹 개발 프로그래머가 될려면 Spring을 배워라

- css는 head에 짜고 js는 body 끝나고 짬 → HTML은 하향식 구조이기 때문에 중간에 에러나면 출력이 안됨