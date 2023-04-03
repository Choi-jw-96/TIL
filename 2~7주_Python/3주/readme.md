#목차 주요 내용
## [Methods](methods.md)
`원본을 유지하지 않는` 모습으로 함수와의 차이를 보임
```
Str
    s.find(x)
    s.index(x)
    s.replace(old,new(,count))

List
    L.append(x)
    L.insert(i, x)
    L.remove(x)
    L.pop(i)
    L.sort()
    L.count(x)

Set
    s.add(x)
    s.pop()
    s.remove(x)

Dictionarty
    d.keys()
    d.values()
    d.items()
    d.get(k, v)
```

## [사용자 정의 함수](User-defined-f(x).md)
```
call & define (붕어빵 틀)
    def foo()... retrun True
input (밀가루, 팥)
scpoe (조리)
output (붕어빵)
```

## [사용자 정의 클래스](user_defined_class.md)
```
class (붕어빵 틀)
instance (각 붕어빵)
attribut (붕어빵 속)
method   (붕어빵 제작)
    class person:    
        def __init__(self, name):   
            self.name = name
    john = person("john")  
```
## [파이썬 응용](python_application.md)
```
`true` 경우 if `조건` else `false` 경우
for i, M in enumerate(M)
[`반복식` for `이름` in `범위`]
{key: value for `이름` in `범위`}
lambda[parameter] : 표현식
```