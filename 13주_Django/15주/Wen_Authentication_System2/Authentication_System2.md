# Authentication_System2

## 1. 개요
## User 객체와 CUD
- 회원 가입
- 회원 탈퇴

## 2. 회원 가입
### userCreationForm()
modelForm

## 5. 비밀번호 변경
### passwordChaingeForm()

## 6. 로그인 사용자에 대한 접근 제한
### request.user.is_authenicated
사용자가 인증 되었는지 여부는 알수 있는 속성
- user : True
- anomymouse : False
### @login_required
인증된 사용자에 대해서만 view함수를 실행 시키는 데코레이터
- from django.contrib.auth.decorators import login_required

