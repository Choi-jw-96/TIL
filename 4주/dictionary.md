# 딕셔너리
## 해시테이블
임의 길이의 데이터를 고정 길이릐 데이터로 메핑하는 함수

- 없다면?
1. 인덱스
2. for 문 => 다 확인해야해
해시함수로 특정 인덱스를 만들어서 값을 입력! => 바로 접근 가능

- 파이썬 딕셔너리는 해시테이블을 사용해서 삭제 삽입 수정 조회가 빠르다
-  언제 사용할까?
1. 문자를 기준으로 값을 찾고싶은 경우
2. 데이터에 대한 빠른 접근이 필요한 경우



## 딕셔너리 문법
### dict[key] = value  
value 삽입/수정

### dict.pop(key,default)
key에 대한 value 삭제 및 반환, 없다면 KeyError
default를 작성하면 keyerror 방지 가능

### dict[key] 
key에대한 value의 반환, 없다면 keyerror

### dict.get(key, default)
key에대한 value의 반환, 없다면 None
default 값 설정 가능

## 딕셔너리 메서드
### .keys()
key 목록에 담긴 dict_key를 반환
### .values()
value 목록에 담긴 dict_value를 반환
#### .items()
key, value를 쌍으루 반환


count[member] = count.get(memer, 0) + 1
==
count_items = count.items()
print(count_items)

==
from collections import Counter
new_count_items = count(members)
print(new_count_item)

print(counter('hello apple hi'))       # 각 문자가 몇개 나왔는지
print(counter('pen pineapple apple pen').most_common())     # P