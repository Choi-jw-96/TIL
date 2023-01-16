# 1.공백으로 구분된 정수
ns = list(map(int, input().split()))
for Ns in ns:
    print(Ns, end = " ")



# 2.공백으로 구분된 문자열
s = list(map(str, input().split()))
for S in s:
    print(S, end = " ")



# 3.테스트 케이스 수와 입력 줄 수가 주어지는 입력
t = int(input())
for T in range(1, t + 1):
    li = int(input())
    for Li in li:
        n = int(input())
        print(n)



#. 4.테스트 케이스 수와 입력 줄 수가 주어지는 입력
t = int(input())

for T in range(1, 1 + t):
    n = int(input())

    for N in range(n):
        a = int(input())
        print(a, a)



# 5. 테스트 케이스 수와 입력 줄 수가 주어지는 입력
t = int(input())
for T in range(1, t + 1):
    li = int(input())
    for Li in range(li):
        s = list(map(str, input().split()))
        for S in s:
            print(S, end = " ")



# 6.
t = int(input())
for T in range(1, t + 1):
    li = int(input())
    for Li in range(li):
        ns = list(map(int, input().split()))
        for NS in ns:
            print(NS, end = " ") 



# 7.
t, li = map(int, input().split())
for T in range(1, t + 1):
    for Li in range(1, li + 1):
        I = map(int, input().split())
        print(*I)       # *은 list를 for한 것 처럼 출력


# # 8.
t, li = map(int, input().split())
for T in range(1, t + 1):
    for Li in range(li):
        a, b = map(int, input().split())
        print(a, b)



# 9. 
t, li = map(int, input().split())
for T in range(1, t + 1):
    for Li in range(li):
        ns = list(map(int, input().split()))
        for NS in ns:
            print(NS, end = " ")