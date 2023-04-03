# 디버깅
## 집중적으로 봐야하는 에러
**branches**
모든 조건이 원하는대로 동작하는지
**for loops**
- 반복문에 진입는지
- 횟수에 맞게 실행하는지
**while loops**
- 반복문에 진입는지
- 횟수에 맞게 실행하는지
- 종료조건이 알맞게 동작하는지
**funcion**
- 함수의 결과
> print(), 개발환경, python tutor 등을 다양하게 활용하자!


## 에러와 예외
### 문법에러 (syntax error)
|문법에러|의미|
|-|-|
|EOL|문자열을 닫거나 열지 않는경우|
|EOF|입력으로 넣지 않고 프로그램이 종료되지 않은 상태|
|invalid syntax|문법상 오류|
|assign to literal|변수이름은 숫자로 시작할 수 없다|

### 예외 (excpetion)
|예외|의미|
|-|-|
|zerodivision| 0으로 나눌수 없음|
|name | 오타, 그래그를 많이 해보자|
|tpye | 들어가면 안돼는 타임 or  agruments 부족 : 필수적 input을 넣지 않을경우 or 초과할 경우 |
|value | 값이 올바르지 않을 때|
|index | 반복문이 더 많이 돌때|
|key | 디션어리에 key가 없을 때|
|modulenotfound|import한 모듈이 존재하지 않을 때|
|improt|모듈엔 있으나 좋재하지 않는 클래스를 가져오는 경우|


## 예외처리
error 대신 except:을 사용해서 프로그램이 터지지 않고 진행시키게 한다
> try 명령문 except 에러시 실행할 예외 코드

# 예외발생시키기
에러를 미리 알려주기위해 예외를 강제 발생
- raise : 표현식 메세지
        실제 프로덕션 코드
- assert : 표현식 메세지
        상태검증용
        
---
## 참조
[실습4](/python/%EC%8B%A4%EC%8A%B54.py) `6번 주목`
[예제4](/python/%EC%98%88%EC%A0%9C4.py)
