#9085
t = int(input())
for T in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))

#10824
A, B, C, D = map(str, input().split())
AB = A + B        # "".join(A, B)
CD = C + D
print(int(AB)+ int(CD))

# AC = str(A + C)
# BD = str(B + D)
# print(AC + BD)


#3009
X = []
Y = []
for comma in range(3):
    x, y = map(int, input().split())
    X.append(x)     # X 사각형
    Y.append(y)     # Y 사각형
for C in [X, Y]:    # X, Y를 따로 받음
    if 2 == C.count(C[0]):      # 같은 수가 2개 이상 있는 수를 걸러냄
        i = C[0]        # 임의의 수를 지정하지 않으면 먼저 지워지는 수 때문에 알맞는 수가 나오지 않음.
        C.remove(i)     
        C.remove(i)
    elif 2 == C.count(C[1]): 
        i = C[1]
        C.remove(i)
        C.remove(i)
print(X[0], Y[0])


# 10952
A, B = 1, 1
while A >= 1 and B <= 9:      # 테스트 케이스가 따로 없으니까 무한으로 돌려야함.
    A, B = map(int, input().split())
    add = A + B
    if add == 0:
        add = ""
    print(add)
    

# 1110
N = int(input())
M  = str(N)     # 시작 N의 값이 변하면 while에서 비교 불가 => M을 따로 지정하고 while에 들어갈수 있게 str로 변경
result = 0
cnt = 0
if len(M) == 1:
    M = "0" + M
while N != M:   # N과 M이 동일할때까지 반복, 시작 M은 문자지만 while 겉치면서 int로 변환하여 맞춤
    result = 0
    for m in str(M):    # 문자로 변경
        result += int(m)
    for R in str(result):
        pass    # 필요없으니 pass
    M = int(m + R)  # m, R의 끝 문자를 더하고 int로 변환
    cnt += 1
print(cnt)


