# input, output(파일의 입출력)

## 활용

### 입력
f = open(file, mode = 'r')
print(f.read())
    mode
    'r' =  읽기 전용
    'w' = 쓰기권한
text = f.readlin()
f.close()


### with
open("hello.txt, 'r', encdoing='UTF8') as f:
    print(type(f))
    txt = f.reading()

## Json
웹 어플리케이션에서 데이터를 전송할 때 사용
데이터를 다수의 프로그래밍 환경에 쉽게 활용 가능한 상태로 변경

### 활용
- 객체(list, dictionary) → json :
```
import json
x = []
json.dumps(x)   # []
```
- json → 객체(list, dictionary)
```
x = json.load(f)
```
## pprint
데이터 구조를 이쁘게 인쇄하는 기능

```
import json
f = open('date/movie.json', 'r', encoding = 'utf8') as f:
    movie = json.load
    print(movie)
    print(type(movie))    # dict
    print(movie['title'])
    print(movie)    # 마지막이 대괄호로 끝나서 리스트 출력


import json
form pprint improt pprint 
f = open('date/movie.json', 'r', encoding = 'utf8') as f:
    movie = json.load
    pprint(movie)
    pprint(type(movie))    # dict
    pprint(movie['title'])
```
---
