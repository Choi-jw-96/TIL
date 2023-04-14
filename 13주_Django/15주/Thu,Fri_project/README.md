# Django Project - 개발자 정보 공유 서비스

### 문지수, 최지원

## 구현 기능

1. 메인페이지
    - navbar
      - 로그인X
        - 회원가입, 로그인
      - 로그인O
        - 로그아웃, id, 회원정보수정
    
    - sidebar
      - 카테고리 별 글 조회
      - 새로운 글 작성
    
    - 반응형 페이지
      - navbar, article
        - md기준 반응형

2. 글 작성 페이지
    - 카테고리를 select input으로 입력

3. detail 페이지
    - 수정, 삭제

4. 회원정보 수정 페이지
    - 회원정보수정, 회원탈퇴

5. 폼 사용
    - PostForm, UserChangeForm
      - field를 지정하고 widget을 사용하여 클래스와 기본값을 삽입
    
    - UserCreationForm
      - UserCreationForm에 존재하지 않는 birthday field가 존재하지 않아 별도로 추가
      - required=False
        - 모든 필드 서브 클래스는 기본적으로 required=True
        - birthday = models.DateField(null = True, blank=True)로 주어졌기 때문에 required=False 가 없으면 빈 값으로 회원가입 불가

6. pagination
    - index 페이지에 글 개수 10개마다 페이지 넘김 구현
    - 다음 페이지가 존재하는 지 확인하고, 반복문 사용하여 페이지 매김 표시
    - 현재 페이지 번호는 active 클래스로 강조
    - 이전 페이지나 다음 페이지가 존재하지 않더라도 버튼을 보이게 위치시키고, 없다면 비활성화

## 문제점 - 해결

1. navbar
    - justify-content: space-between; 적용이 되지 않음
      - style에서 전체 div에 margin: auto;를 준 것이 원인
    
    - 창의 크기가 줄었을 때, 
      - navbar 오른쪽의 버튼과 {{ user }}가 column 형식으로 아래로 내려가 구조 무너짐
        - 따로 div로 묶어 flex를 주어 해결

      - navbar 내의 div 구조가 무너져 nav를 벗어나는 문제가 발생
        - nav의 높이를 100%로 바꿔 해결
    
      - row, col을 이용하여 반응형으로 바꾸는 시도 중 navbar 오른쪽의 div는 잘 작동하나 왼쪽은 문제가 생김
        - container div에 mx-auto를 주어 가운데 위치로 옮김
        - a태그 가지고 있는 div에 justify-content-start 를 주어 Information a 태그가 왼쪽으로 정렬되게 함
      
    - sticky 적용이 안되는 문제
      - sticky 적용한 nav가 header내에 존재했었지만, navbar 높이가 고정이 아니었기 때문에 문제 발생
        - nav의 상위에 존재하는 header를 지워 해결
    
2. article
    - sidebar section과 content section이 row-col을 주어도 오른쪽 공간이 많이 남는 문제 발생
      - article에 container-fluid를 주고, section 2개를 묶고 있는 div에 container를 준 것이 원인 => article class를 container로 수정하여 해결

    - navbar와 article이 겹쳐짐
      - navbar position을 fixed에서 sticky로 바꾸어 해결
    
    - 창이 줄어들 때 sidebar h3와 li요소의 텍스트가 아래로 내려감
      - white-space: nowrap; 로 해결

    - 창의 크기가 커졌을 때
      - article의 요소가 계속 오른쪽으로 당겨옴
        - article margin을 없애고, 상단의 margin만 주어 해결

3. detail - NoReverseMatch 오류
    - url 태그 안 method 자리에 pk값 적어 오류
    - views.py에서 변수 값 오류

4. 메인페이지로 향하는 BACK 버튼 생성 중 form 안의 input과 한 줄에 위치시킴
    - form 안에 BACK버튼을 위치시키면 form의 url과 충돌하여 작동 X
      - onclick 사용하여 해결

5. pagination
    - previous, next 버튼이 이전페이지나 다음페이지가 존재하지 않으면 나타나지 않음
      - 현재 페이지에 이전 페이지가 없으면 disabled 클래스가 이전 버튼 요소에 추가되어 비활성화시킴 + next 버튼도 같은 방식
      - disabled 클래스 사용하여 해결