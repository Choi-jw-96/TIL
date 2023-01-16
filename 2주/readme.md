#목차 주요 내용
## [Python 기초](Python_%EA%B8%B0%EC%B4%88.md)
- 명령어를 문법적으로 컴퓨터에게 전달하는 언어 중 하나
- 객체로 모두 구현 되는 `객체 지향` 프로그래밍
![vo](variable_object.png)
`= : 객체를 변수에 할당할 때 사용`
- 객체의 종류
![object](Object.png)
```
숫자형
- int
- boolean type
    / : 나누기
    // : 몫
    % : 나머지
    < : 미만

시퀀스형
- str
    \n : 줄 바꿈
-list
    s[0:5] : s의 0~4번째까지
    s + t : s와 t를 공백없이 이어붙이기
    s * n : s를 n번 생성
    시퀀스형 연산자의 시작은 `0부터` 음수는 뒤에서 `-1부터`
-range
    range(0,5,2)[::-1] == [4. 2, 0]

컬렉션형
- dictionary(딕셔너리) : 유일한 값 모음
```
---

## [Python 제어문](Python_%EC%A0%9C%EC%96%B4%EB%AC%B8.md)
```
조건문
- if:...elif:...else:

반복문
- while : 조건에 해당 시 종료

- for : 모든 객체를 순회 후 종료
    for.. in...:
    end = "" : 일렬로 정렬
    

- 반복제어
    break : 조건 후 종료
    continue : 조건 해당사항은 넘기고 순회 후 종료
```

[pythontutor](https://pythontutor.com/)

---
## [함수](%ED%95%A8%EC%88%98.md)

```
len(s)
sum(iterable, strart =0)
max(iterable)
min(iterable)
map(int, input().split)
```
## [컬랙션](collections.md)
```
 Dictionary (딕셔너리)
    key : value가 쌍으로 이뤄진 모음
    반복문은 key를 활용하여 반복 => 같은 key는 카운팅된다
    
Module(모듈)
    특정 기능을 하는 `코드를  파일`로 작성한것
    - random
    - datetim
    - os
library(라이브러리)
    다양한 `패키지를` 하나의 `묶음
    - random.sample(popultion, k)
```

## [에러 / 통과](Error_ms.md)
```
EOL
EOF
invalid syntax
assign to literaㅣ
try... except...
```

## [입출력](input_output.md)
Json
