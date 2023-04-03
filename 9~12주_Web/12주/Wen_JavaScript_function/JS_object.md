# 객체

## 개요
### object
키로 구분된 데이터 집합을  저장하는 **자료형**(객체지향어 같은게 아님) (= dict)

### 구조
```javascript
const user = {
  name: 'sophia', 
  age: 30,
  'key with space': true,
}
```
- 중괄호를 이용해 작성
- 중괄호 안에 key: value 쌍으로 구성괸 속성(property)를 여러개 넣을 수 있음
- key는 문자형, value는 모른 자료형 허용
- ',' 는 속성 추가, 삭제, 이동에 용이해서 씀(사용 안해도 됨)

## [속성](object_01.html)
### 조회
- 점표기법
```javascript
console.log(user.age)
```
- 대괄호 표기법
```javascript
console.log(user['key with space'])
```

### 추가(없는 자료)
```javascript
user.address = 'korea'
```

### 수정(있는 자료)
```javascript
user.age = 40
```

### 삭제
```javascript
delete user.address
```

### 존재 여부 확인
```javascript
console.log('age' in user)
```
### 단축 property
```javascript
    const age = 30
    const address = 'korea'

    const newUser = {
      age,
      address,
    }
```

### 계산된 속성
```javascript
    const a = 'hello'
    const b = 'bye'

    const bag = {
      [a]: 5,
    }
```


## [객체와 함수](object_02.html)
### Methon
객체 속성에 정의된 함수
```javascript
console.log(person.greeting())
```
메서드는 객체를 '행동'할 수 있게 함

#### this
함수나 메서드를 호출할 객체를 가리키는 키워드
```javascript
  const person = {
    name: 'Sophia',
    greeting: function () {
      return `hello, ${this.name}`
    },
  }
```
(**함수 내**에서 객체의 속성 및 메서드에 접근하기 위해사용)

JS에서 함수르르 **호출하는 방법**에 따라 가리키는 대상이 다름
1. 단독 호출 -> **전역객체**
2. **메서드** 호출 -> **메서드를 호출한 객체**

#### Nested 함수에서의 문제점과 해결책
화살표함수는 자신만의 this를 가지지 않기때문에 외부 함수에서 this값을 가져옴

**메서드 정의할때는 화살표 함수 금지(메서드 호출 객체가 대상이니까)**

### this 특징
호출 전 까지 값이 할당되지 않고, 호출 시 결정 (동적) 

---
## 참고
### Json(Javascript Objest Noatation)
- key-value형태로 이루어진 자료표기법
- 형식은 문자열
- 자료형으로 변경이 필요
```javascript

```