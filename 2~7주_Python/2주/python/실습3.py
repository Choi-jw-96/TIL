# 1
a = int(input("정수를 입력하세요 > "))

if a < 0:
    a *= -1
print (a)



# 2
number_list = [1, 2, 3, 4, 5]

T = 0
for N in number_list:
    T += 1
print(T)



# 3
number_list = [1, 2, 3, 4, 5]

T = 0
for N in number_list:
    T += N
print(T)



# 4
number_list = [2, 4, 6]

S = 0
for s in number_list:
    S += s
L = 0
for l in number_list:
    L += 1

print(S / L)



# 5
number_list = [1, 2, 3, 4, 5]

M = 1
for m in number_list:
    M *= m
print(M)



# 6
number_list = [1, 2, 3, 4, 5]
n = number_list[0]
for M in number_list:
    if M >= n:
        n = M
print(n)



# 7
number_list = [1, 2, 3, 4, 5]
n = number_list[0]                      # n = list안에서 정한다(list 중 젤 작은 수이니까)
for M in number_list:                   # list를 쪼개줘
    if M <= n:                          # M이 n보다 작거나 같다면    
        n = M                           # M을 n에 넣어줘!! (==가 아니다 주의)
print(n)