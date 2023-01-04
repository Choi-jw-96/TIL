# 제어문
- 특정 상황에 따라 계속하여 실행하는 제어가 필요함
## 조건문
### 기본
- 조건식(참/거짓)과 함께 사용

### 형식
if ``:``

elif ``:``

else``:``
```
d = 80
if d > 150 :
   print("매우나쁨")
   if d > 300:
      print("실외활동 금지")
elif d > 80 :
   print("나쁨")
elif d >30 :
   print("보통")
else :
   if d >= 0:
       print("좋음")
   else:
       print("값이 잘못되었습니다.")

```

## 반복문
- 특정 조건을 도달할 때까지, 반복되는 일련의 문장

### 종류
1. while문
- 종료 ``조건에 해당``하는 코드르르 통해 종료
```
n = 10
t = 0
a = 0
while n >= a:
    t += a
    a += 1
    print(t, a)
print(t)

```


2. for문
- ``모든 객체를 순회`` 후 종료
- 별도의 종료조건 필요 없음

```
t = 0
a = int(input())


for A in range(1, a + 1):
    t += A
print(t)


for num in range(4) :
   print(num**2)
0
1
4


for num in range(4) :
   print(num**2, end = " ")
0 1 4


a = "pineapple"
for i in range(len(a)) :
    print(i, a[i])
0 p
1 i
2 n
3 e
4 a
5 p
6 p
7 l
8 e


word = 'apple'
for char in word:
   # print('char')
   if char == 'a':
      print('1')
1
```
```
while for 차이
- while
n = 10
t = 0
a = 0

while n >= a:
    t += a
    a += 1
    print(t, a)
print(t)

- for
t = 0
a = int(input())


for A in range(1, a + 1):
    t += A
print(t)
```



3. 반복 제어


- break

반복문 종료
```
word = 'apple'
for char in word:
    print('char')
    if char == 'a':
      print('1')
      break # 반복 종료
else  # break 되지 않았다면 실행해줄게
    print('0')
a를 만나면 1을 출력하고 종료하세요


is_end = False
for char in word:
    if char == 'e':
        print(1)
       is_end = True
       break
# if is_end:
#    print(1)
 else:
    print(0)
```


- continue

해당 코드블록은 수행하지 않고, 다음 반복 수행
```
word = "banana"
for char in word:
   # print('char')
    if char == 'a':
      continue    
      #bnn => a를 만나면 실행 없이 다음 반복 실행으로 넘어간다
    print('1')
1
1
1
```

---
참고
[pythontutor](https://pythontutor.com/)


[실습2](python/%EC%8B%A4%EC%8A%B52.py)


[예제2](python/%EC%98%88%EC%A0%9C2.py)