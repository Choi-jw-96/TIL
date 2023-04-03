# collection(컬렉션)
## Dictionary (딕셔너리)
- ``key : value``가 쌍으로 이뤄진 모음
- key는 분변형 자료 (str, int, float, bloolean, tuple, range) 
- values는 형태 무관 (List, dictionary...)
- ``,``으로 요소 구분 
- 변경가능, 반복가능


### 생성
- key와 value가 쌍으로 이루워진 구조
- 기존값음 `변경 가능`
- `append 없이` key와 value을 `추가`하면 없이 추가할 수 있다
- `.pop`을 활용하여 `삭제`
- 반복문은 `key를 활용하여 반복` => 같은 key가 ``카운팅`` 된다 (실습4의 6반)

```python
#키 - 이름, 값 - 전화번호
phone_book = {
    "피자헛" : "1588-5588",
    "전화번호" : "114",
    "대리운전" : "1577-1577"
}

phone_book["김탁희"] = "101-1234-1234"      # 추가
phone_book["김탁희"] = "010-1234-1234"      #변경

print(phone_book["피자헛"])

for name in phone_book:    # name은 변수의 이름
    print(name)    # key만 줌 = 피자헛
    print(phone_book[name])    # vaule만 줌 = 1588-1588
```



## Module(모듈)
### Module(모듈)
특정 기능을 하는 `코드를  파일`로 작성한것
- random
- datetim
- os
### Package(패키지)
다양한 `파일(모듈)`을 하나의 `폴더`로
### library(라이브러리)
다양한 `패키지를` 하나의 `묶음`

|random|무작위 요소 선택|
|-|-|
|.randint(a, b)|a와 b 사이의 정수 반환|
|.choice(seq)|시퀀스에서 임의의 요소 반환|
|.suuggle(seq)|시퀀스를 섞음|
|.sample(popultion, k)|k 길이의 결과를 반환|

|datetime|날짜와 시간|
|-|-|
|.date(year, month, day)|모든인자 필수+ 정수, ()안의 시간을 표시|
|.date.today()|현제 지역 날짜|
|.datetime.today()|현재 지역 datetime|

|Os|운영체제 조작을 위한 인터페이스 제공|
|-|-|
|.listdir(path=".")|path에 주어진 폴더에 있는 항목들이 이름을 달고 리스트로 반환|
|.mkdir(path))|path라는 폴더를 만듦|
|.chdir(path))|path를 변경|

```python
import os
print(os.listdir())
```



### pip
위를 관리하는 `관리자`
저장된 외부 패키지를 설치하도록 도와 줌

>import 와 from...import를 사용


```python
import random    # 모듈을 가져옴
menu = ["밥", "빵", "면"]
print(random.choice(menu))
```
```python
import random
s = range(1, 46)
a = random.sample(s, 6)
print (a)

for i in range(5):
    import random
    s = range(1, 46)
    a = random.sample(s, 6)
    print(sorted(a))

students = ["m", "h", "s", "j"]
print(students)
a = random.shuffle(students)
print(a)
```
```python
import datetime
print(datetime.datetime.now())    # 시간까지

d = datetime.date(2023, 1, 1)    # 날짜까지
print(type(d))
print(d.year)
print(d.day)

end = datetime.date(2023, 6, 14)
print(end - d)
```


---
## 추가정보

.sort() : 메서드
return : None > 원본을 바꾼다
해당 리스트 차례를 정렬 

sorted() : 함수
정렬된 리스트

---
## 참조
[실습4](/python/%EC%8B%A4%EC%8A%B54.py) `6번 주목`
[예제4](/python/%EC%98%88%EC%A0%9C4.py)
