# 사용자 정의 클래스
1. class (붕어빵 틀)
2. instance (각 붕어빵)
3. attribut (붕어빵 속)
4. method   (붕어빵 제작)


## 객체 지향 프로그래밍
- 여러 객체들과의 상호작용을 파악하는 프로그래밍 방법
- 데이터와 메소드를 분리한 추상화 구조
    
    ↔ 절차지향 프로그래밍 : 데이터와 함수로 인한 변화


### 객체 
python은 모든 객체로 이뤄져 있다.

→ 객체는 type의 instance

1. type : 어떤 연산자와 method로 가능한가?
2. attribute : 어떤 데이터를 가지는가?
3. method : 어떤 함수를 할 수 있는가?

> class ...:    
    def__init__(self,...):   
        self....=..


### Class 
class를 가지고 instance(객체)를 생성한다
class에서의 내부정의는 모든 instance가 같은 속성을 지니게 함

리스트 : [1, 2, 3], ["1"]
> class person: pass      
    print (type(person()))  
    # main.person → 객체의 타입은 person

```
- @classmethod..(cls) : class를 활용/조작
- ..(self) : instance를 활용/조작
- @staticmethod : instance, class 활용/ 조작 X
```
#### 상속
두 클라스 사이에 부모 - 자식 관계

두개 이상의 클래스를 상송받을 수 있음 (중복시 순서에 의해 결정)

부모에 정의된 것을 활용하여 오버라이딩하여 활용

상속받은 클래스에서 같은 이름의 매서드로 덮어씀
> isinstance(object, classinfo)     
isubclass(class, classinfo)    
.super() : 부모클래스를 사용하고 싶은경우

#### Attribute
클래스의 객체들이 가지게 될 데이터
>class person:  pass  
    person1 = person("지민")    
    # 지민

#### Method
클래스에 공통적으로 적용가능한 함수

##### 객체 비교하기
- `==` : 내용이 같을 때 but 엄연히 다른 객체
- `is` : 두 변수가 완전히 같은 객체

### Instance
instance = 객체

- instance 변수 : 각각의 instance의 attribute
> class person:    
    def __init__(self, name):   
        self.name = name    # instance의 변수 정의  
john = person("john")   
print(john.name)    # instance 변수 접근    
john.name = "Johm Kim" # instance 변수 할당

- instance method 
```   
-instance의 변수를 사용 / 값 설정하는 메소드 
-클래스 내부에 정의되는 method의 기본
-호출 시, 첫 인자로 self(instance 자기 자신, gloal rules)에 전달
```
- 생성자 method
```
생성 시 자동 호출 메서드
__init__
```

- 소멸자 method
```
소멸 시 호출되는 코드
    def __del__(self):....
```

- 매직 method
특수 동장을 위해 만들어진 메소드 
> `__str__(self)` : 객체 출력을 지정    
`__gt__(self)` : 부등호 연산자
---
[연습](실습/%EC%97%B0%EC%8A%B5_2.py)