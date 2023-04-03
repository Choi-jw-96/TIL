# 메서드와 데이터 타입
## methods
`객체`에 적용하는 특정 함수
`원본을 유지하지 않는` 모습으로 함수와의 차이를 보임
`변경가능한 객체`에서 사용가능
> type.methods()
### 데이터 타입별 메서드

#### Str
1. 탐색 / 검증

|문법|설명|
|-|-|
|s.find(x)|x 위치 반환, `없다면 -1`|
|s.index(x)|x 위치 반환, `없다면 error`|
|s.isalpha()|알파벳 문자 여부|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|
|s.istitle()|타이틀 형식 여부|
* `is`가 들어가면 boolean형태


2. 변경

|문법|설명|
|-|-|
|s.replace(old,new(,count))|특정글자를 변경 (해당 개수만큼 실행)|
|s.strip()|양쪽 끝의 공백, 특정문자 제거|
|s.split()|공백, 특정문자 기준 분리|
|''.join([iterable])|iterable끼리 합침|
|s.capitalize()|첫 글자를 대문자로 변경|
|s.title()|공백이후 대문자로 변경|
|s.upper()|모두 대문자로 변경|
|s.lower()|모두 소문자로 변경|
|s.swapacase()|소문자와 대문자를 서로 변경|

---

#### List

|문법|설명|
|-|-|
|L.append(x)|마지막 항목에 추가|
|L.insert(i, x)|i항목에 x 삽입|
|L.remove(x)|첫 x를 제거, 없다면 error|
|L.pop()|마지막 항목을 반환 후 제거|
|L.pop(i)|i항목을 반환 후 제거|
|L.clear()|L항목 모두 제거|
|L.extend(m)|m(여러개)의 모든 항목들의 리스트 끝에 추가|
|L.index(x, start, end)|앞에있는 x의 i를 반환|
|L.sort()|오름차정렬|
|L.reverse()|순서를 반대로 뒤집음|
|L.count(x)|리스트에 x의 객수 반환|

* 내림차순은 L.sort(reverse=True)

---

#### Set
중복, 순서 X

|문법|설명|
|-|-|
|s.copy()|세트 복사본 반환|
|s.add(x)|x가 없다면 추가|
|s.pop()|랜덤 반환 제거, 없다면 keyerror|
|s.remove(x)|마지막 항목을 반환 후 제거|
|s.discard(x)|x가 있다면 삭제|
|s.update(t)|t에 있는 모든 항목 중 없는 걸 추가|
|s.clear()|모든 항목 제거|
|s.isdisjoint(t)|t 중 하나라도 없다면 True|
|s.issubset(t)|s가 t의 하위 세트면 True|
|s.issuperset(t)|s가 t의 상위 세트면 True|

---

#### Dictionary

|문법|설명|
|-|-|
|d.keys()|모든 키를 담은 뷰 반환|
|d.values()|모든 값을 담은 뷰 반환|
|d.items()|키-값을 담은 뷰 반환|
|d.pop(k)|k반환 후 삭제, 없다면 keyerror|
|d.pop(k, v)|k반환 후 삭제, 없다면 v 반환|
|d.get(k))|k 반환, 없다면 None|
|d.get(k, v)|k 반환, 없다면 v반환|
|d.clear()|모든 항목 제거|
|d.update()|값을 메핑하여 업데이트|


---
참고
[methods](실습/1.methods_P.py)
[예제](실습/%EC%97%B0%EC%8A%B5.py)

