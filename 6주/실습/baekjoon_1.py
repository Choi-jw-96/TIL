#1225
import sys
A, B = map(str, sys.stdin.readline().split())
total = 0

A= list(A)
B = list(map(int, B))
 
for a in A:
    add = int(a) * sum(B)
    total += add
print(total)


# 시간 초과
for a in A:
    for b in B:
        add = int(a) * int(b)
        total += add
print(total)



for i in range(0, len(A)):
    for I in range(0, len(B)):
        add = int(A[i]) * int(B[I])
        total += add
print(total)



#2483
star =int(input())
print(*["*" * _ for _ in range(1, star + 1)], sep= "\n")



#2739
num = int(input())

for i in range(1, 10):
    print(f'{num} * {i} = {num * i}')



#2953
P = []
t = 0 
num = 0
for _ in range(5):
    p = list(map(int, input().split()))
    P.append(p)
for i in range(5):
    
    if t < sum(P[i]):
        t = sum(P[i])
        num = i + 1
print(num, t)



#2669
square = []
add = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # 한칸씩 움직이면서 포함되는 xy를 체크한다
    for i in range(x1, x2):
        for j in range(y1, y2):
            # i j까지 사각형을 이루는 모든 점을 표시한다. => 칸당 면적은 1
            square.append((i,j))

# set으로 중복되는 값을 지워준다.
square = set(square)
# 중복되지 않는 면적을 모두 더한다.
print(len(square))