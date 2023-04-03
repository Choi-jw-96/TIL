# 이벤트 만들기

## 개요
사건을 통해 특정 동작을 수행한다

## 이벤트
무언가 일어났다는 신호, 사건 (마우스, 인풋, 키보드, 터치 등)

DOM요소는 event를 받고 받은 event를 '처리(event handler)'할 수 있음

### [event hander](button.html)
이벤트가 발생했을 때 실행되는 함수

- 요소.addEventListener(type, handle) 
  : 특정 이벤트를 DOM 요소가 수신 할 때 마다 콜백 함수를 호출

  [type](https://developer.mozilla.org/en-US/docs/Web/Events) : 이벤트
  
  handle : 콜백함수


## 이벤트 핸들러 활용
### [click이벤트 ](click_event.html)
버튼을 클릭 시 1씩 오르게

### [input이벤트](input_event.html)
사용자 입력값을 실시간을 출력

### [click&input](click_input_event.html)
사용자가 입력핪을 실시간으로 출력
+ 버튼 클릭 시 스타일 변경

### [복사 금지](prevent_event.html)
- .preventDefaul() : 현재 기본동작 중단
- alter : 경고창

### [todo](todo.html)
할일을 입력하고 클릭하면 요소 생성
안하면 경고알림

### [로또 번호 생성기](lottery.html)



---
## 참고
[jsDeliver](https://www.jsdelivr.com/)
[lodash](https://lodash.com/)