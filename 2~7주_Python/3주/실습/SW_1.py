# 2029
t = int(input())
for T in range(1, t+1):
    a, b = map(int, input().split())
    c = a // b
    d = a % b
    print(f"#{T} {c} {d}")



# 2071
t = int(input())
for T in range(1, t+1):
    Ns = list(map(int, input().split()))
    A = round(sum(Ns) / len(Ns))   
    print(f'#{T} {A}')



# 1938
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)



# 2046
n = int(input())
# print("#" * n)

for N in range(n):
    print("#", end = "")


# 2068
t = int(input())
M = 0
for T in range(1, t+1):
    Ns = list(map(int, input().split()))
    for N in Ns:
        if N >= Ns[0]:
            M = N
    print(M)


t = int(input())
M = 0
for T in range(1, t+1):
    Ns = list(map(int, input().split()))
    M = max(Ns)
    print(f'#{M}')
