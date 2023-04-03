# JavaScript and DOM

## 개요
**웹 브라우저에서의 JavaScript를 학습**
웹 브라우저에 내장된 JavaScript엔진에 의해 브라우저에서 실행

### 실행 환경
1. HTML
2. js 확장자파일
3. 브라우저 console
---
- console.log() : 출력(=print)


## DOM 기본개념
### DOM
document object model(문서 객체 모델)

웹페이지를 구조화된 객체로 제공하며 **프로그래밍 언어가 웹페이지를 사용할 수 있게** 연결시킴

HTML + CSS + JavaScript를 묶어서 조작할 수 있는 방법을 제공하는 API

브라우저는 HTML문서를 해석하여 **DOM tree**라는 객체의 **트리로 구조화**

DOM에서는 모두 document객체에 있는 모든 요소, 속성, 텍스트가 하나의 객체

웹페이지를 동적으로 만드는 것 == 웹 페이지를 **조작(생성, 추가, 삭제)**하는 것

조작 순서?
- 조작하고자 하는 요소를 선택 or 탐색
- 콘텐츠, 속성을 조작

### document object
- Domtree의 진입점
- 웹 페이지 객체
- 페이지를 구성하는 모든 객체 요소를 포함

---
HTML 변경 : title값 변경
const N = ~


## [DOM quert(선택)](01_select.html)
| 요소 갯수 | 코드 |
|-|-|
|요소 하나만 선택|document.querySelector()|
|여러개 선택|document.querySelectorAll()|

## DOM Mainpulation(조작)
### 속성(attribute)
| 클라스 속성 조작 | 코드 |
|-|-|
|추가|E.classList.add()|
|제거|E.classList.remove()|

| 일반 속성 조작 | 코드 |
|-|-|
|반환|E.get.Attribute()|
|속성값을 새로 설정|E.setAttribute()|
|제거|E.removeAttribute()|

### HTML 콘텐츠 조작| 클라스 
|| 코드 |
|-|-|
|변경|E.textContent = ""|

### DOM요소 조작
|| 코드 |
|-|-|
|생성|E.createElement()|
|추가|E.appendChild()|
|삭제|E.removeChild()|

### DOM Mainpulation
E.style... = ""