# 1
a = str(input("문자열을 입력하세요 > "))
c = 0

for A in a:
    if A == "e":
        c += 1
print(c)



# 2
a = str(input("문자열을 입력하세요 > "))
b = ["A", "a", "E", "e", "O", "o", "U", "u", "I", "i"]
c = 0

for A in a:
    if A in b:
        c += 1
print(c)



# 3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

a = 2023  - int(dict_variable["생년"]) + 1
print(f"나이 : {a}")



# 4
d = {}
n = input("이름을 입력하세요 > ")
p = input("전화번호을 입력하세요 > ")
h = input("거주지을 입력하세요 > ")
d["이름"] = n
d["전화번호"] = p
d["거주지"] = h
print(d)
for D in d:
    print(f"{D} : {d[D]}")



# 5
n = input("이름을 입력하세요 > ")

d = {n : {}}

p = input("전화번호을 입력하세요 > ")
e = input("이메일을 입력하세요 > ")
h = input("거주지을 입력하세요 > ")

d[n]["전화번호"] = p
d[n]["이메일"] = e
d[n]["거주지"] = h

print(d)



# 6
# dict 힌트 받고 작성한 코드
a = input()                     
dict = {}                       # 딕션어리 사용해야 반복문자를 뭉칠 수 있음
c = 0                           

for A in a:                     # 입력된 글자를 반복
    if a.count(A) >= 1:         # 입력된 글자를 셈
        c += a.count(A)
    dict[A] = c                 #글자와 글자수를 dict에 저장
    c = 0                       # 입력된 c를 초기화 후 count 반복
for name in dict:               # dict를 반복해
    print(name, dict[name])     # 글자, 글자수 출력
    

# 다른학생 보고 만들어본 코드
a = input()                     
dict = {}
c = 0

for A in a:
    c = 0                       # c 초기화
    for I in a:                 # 비교군을 다시 만든다
        if A in I:              # A와 I 비교
            c += 1              # 같다면 + 1
        dict[A] = c
for name in dict:
    print(name, dict[name])


a = input()
d = {}

for A in a:
    c = 0
    for N in a:
        if A == N:
            c += 1
        d[A] = c
for D in d:
    print(D, d[D])




#실패코드
# a = input()
# dict = {}
# c = 0

# for A in a:
#     for N in range(len(A)):
#         if A.count(a[N]) == True:
#             c += 1
#         dict[A] = c
# for name in dict:
#     print(name, dict[name])
    
