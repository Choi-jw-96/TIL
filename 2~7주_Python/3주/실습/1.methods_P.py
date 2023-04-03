# 1 문자열 입력 + e에 위치 출력
a = input("문자열을 입력하세요 > ")
num = 0
if 'e' in a:    # e의 유무부터 확인
    for A in a:
        if A != 'e':    # e가 없다면
            num += 1
        else:   # e가 나오면 종료
            break
else:
    num = -1
print(num)

# try:
#     num = A.index("e")
# except:
#     num = -1
# print(num)

# 2
a = list(map(str, input("문자열을 입력하세요 > ").split()))
dir = {}
for A in a:
    if A not in dir:    
        dir[A] = 1      # dir에 A : 1
    else:       
        dir[A] += 1     # 있다면 +1
for K in dir:
    print(K, dir[K])    # A n



# 3
a = input("문자열을 입력하세요 > ")
s = ""
for A in a:
    if A != 'e':
        s = A
    else:
        s = ""
    print(s, end = "")



# 4
a, b = map(str, input("문자열을 입력하세요 > ".split))
c = 0
for A in a:
    if A == b:
        c += 1
print(c)



# 5
a, b, c = map(str, input("문지열을 입력하세요").split())
print(a + "-" + b + "-" + c )



# 6
a = input("양의 정수를 입력하세요 > ")
t = 0
if int(a) >= 0:
    for A in a:
        t += int(A)
else:
    t = -1
print(t)

# if a < 0:
#     t = -1
# else:
#     while a > 0:
#     t += a % 10
#     a //= 10
#     print(t)
