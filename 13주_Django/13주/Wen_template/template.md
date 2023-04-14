# Temlplates

## Temlplate system
데이퍼 **표현**을 제어하면서, **표현**과 관련된 로직을 담당

### Djago Template Language(DTL)
: temlpate에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템
if/for을 사용할 수 있지만 python코드가 아니다.

- 변수
- 필터
- 태그
- 주석

#### 변수
```html
{{ varialbe }}
```
- 딕셔너리 타입으로 넘겨받을 수 있음
- key가 면수명이 됨
- dot(.)을 사용하여 변수 속성에 접근 가능

#### 필터
```html
{{variable|filter}}
```
- 표시할 변수를 수정할 때 사용
- chained 가능, 일부틑 인자를 받이고 한다

#### 태그
```html
{% tag %}({% if %} {% end if %})
```
- 논리 & 반복 문을 수행
- 시작과 종료 태그가 필요

#### 주석
```
{% comment %}....{% comment %}
```
주석 처리 한다


## 템플릿 상속
**페이지의 공통요소를 포함**하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 **'skeleton'탬플릿을 작성하여 상송구조를 구축**

```python
setting
TEMPLATES = [{
  'DIRS' : [BASE_DIR / 'templates',],
}]

```

### extends tag 
자식 템플릿이 부모템플릿을 확장한다는 것을 알림
**무조건 최상단에 작성(2개 이상 상속 불가)**

### Block tag
하위 템플릿에서 재정의 할 수 있는 블록을 정의


## 요청과 응답 with HTML form
HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

### form element
사용자로부터 할당된 데이터를 서버로 전송
웹에서 사용자 정보를 입력하는 여러방식을 제공

### action & method
- action : 데이터를 어디로(URL 지정)
- method : 어떤 방식으로 보낼지(HTTP methods(GET, POST) 지정)

---
- GET :브라우저 히스토리에 남는다.
- POST : 브라우저 히스토리에 안 남는다.


### input element
사용자의 데이터를 입력받을 수 있는 요소

### name 
**input의 핵심속성**
데이터를 제출할 때 서버는 name속성에 설정된 값을 통해 **사용자가 입력한 데이터에 접근 할 수 있음**
```
http://127.0.0.1:8000/search/?message=django
name = "message" :key
input = "django" : value
```


## 요청과 응답 활용
- form 데이터는 어디에 들어있을까?
: HTTP request 객체에 들어있다 (views)