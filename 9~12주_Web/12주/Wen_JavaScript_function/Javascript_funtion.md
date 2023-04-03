# 함수

## 개요
참조 자료형의 하나

### 구조
- 이름
- 매개변수
- body를 구성하는 statement


## [함수 정의](funtion.html)
### 선언식(function declartaion)
- 이름이 필수로 필요
- var처럼 아래 만들어 놓으면 끌어 올려짐(유지보수 bad)
```javascript
  function ... () {
    return
  }
```


### 표현식(funtion expression)
- 익명 함수
- 사용 권장
```javascript
  const ... = function () {
  return
  }
```

### 기본함수 매개변수
값이 없거나 undefind가 전달 될 경우 이름이 붙는 매개변수
```javascript
  const ... = function () {
    return 0
  }
```


### 나머지 매개변수
무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법
```javascript
  const myFunc = function (num1, num2, ...restArgs) {
    return [ num1, num2, restArgs]
  }
```

### 화살표 함수 표현식
함수 표현식의 간결한 표현법
```javascript
// 1 무조건 가증
  const arrow1 = (name) => {
    return `hello, ${name}`
  }
// 2 표현식이 한줄이라면 가능
  const arrow2 = (name) => `hello, ${name}`
```
