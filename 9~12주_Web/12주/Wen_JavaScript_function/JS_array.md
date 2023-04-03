# 배열
## 개요

### Object
키로 구분괸 데이터의 집합을 저장하는 자료형
**이제는 순서가 있는 collection이 필요하다**

### Array
순서가 있는 데이터 집합을 조장하는 자료구조

### 구조
- 대괄호를 이용해 작성
- length를 사용해 배열에 담긴 요소가 몇개인지 알 수 있음
- 배역 요소의 자료형엔 제약이 없음
- 배역의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음


## [배열과 메서드](array.html)
|메서드|기능|역할|
|-|-|-|
|push, pop|배열 끝 요소를 추가, 제거|요소 추가, 제거|
|unshift, shift|배열 앞 요소를 추가, 제거|요소 추가, 제거|
|forEach|**인자로 주어진 함수**(콜백함수)를 **배열 요소** 각각에 대해 실행|**반복**|
|map|배열 요소 전체를 대상으로 함수(콜백함수)를 호출하고, 함수 호출결과를 **새로운 배열 함수로 반환**|반복, 변형|

### forEach구조
```javascript
array.forEach(function (item, index, array){
  // do something
})
```
- item : 배열 요소
- index : 배열 요소의 인덱스(선택사힝)
- array 배열(선택사항)
반복문!

#### 콜백함수
다른 함수에 인자로 전달되는 함수
- 재사용 측면 : 동작의 자유성, 간결성, 가독성
- 비동기적 측면 :


### map
forEach + 반환
```javascript
const result = array.map(function (item, index, array){
  // do something
})
```


### 정리
- 배열의 본질은 객체
- 배열의 요소를 대괄호 접근법을 사용해 접급하는 건 객체 문법과 같은
- 다만 배열 키는 숫자
- 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드를 제공

---
## 참조
### 배역 순화 종합
|방식|특징|비고|
|for loop|배열 + 인덱스로 요소 접근|break continue 가능|
|for...of|배열 요소에 바로 접근|break continue 가능|
|forEach|배열 + 인덱스로 각각 요소 접근, 유지보수 좋음|break continue 불가능, 사용권장|
