#  2072
t = int(input())
for T in range(1, t+1):
    ns = list(map(int, input().split()))
    A = 0
    for Ns in ns:
        if Ns % 2 == 1:
            A += Ns
        else:
            continue
    print(f'#{T} {A}')



# 2056 0101년도가 출력이 0이 빼고 됨
t = int(input())
for T in range(1, t+1):
    ns = input()
    yyyy = ns[0:4]
    mm = ns[4:6]
    dd = ns[6:8]
    if int(mm) == 0:
        print(f'#{T} {-1}')
    elif int(mm) <= 12:
        if int(mm) <= 7:
            if int(mm) % 2 == 1:
                if int(dd) > 31:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
                 
            elif int(mm) == 2:
                if int(dd) > 28:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
            else:
                if int(dd) > 30:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
        else:
            if  int(mm) % 2 == 0:
                if int(dd) > 31:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
                     
            else:
                if int(dd) > 30:
                    print(f'#{T} {-1}')
                else:
                    print(f'#{T} {yyyy}/{mm}/{dd}')
 
    else:
        print(f'#{T} {-1}')



# 2043
P, K = map(int, input().split())
c = 1
while K < P:
    K += 1
    c += 1
print(c)



# 1933
n = int(input())
I = []
for N in range(1, n+1):
    if n % N == 0:
        I.append(N)
print(*I)



# 1288 
t = int(input())
for T in range(1, t+1):
    s = int(input())
    n = []
    a = 0
    while len(n) < 10:      # 갯수 10보다 작으면 계속 돌려
        a += s
        for A in str(a):
            if A not in n:
                n.append(A)
    print(f'#{T} {a}')