# 1.
n = int(input("정수를 출력하세요."))
print(n)

# 2. 
s = input("단어를 구분해서 출력하세요.").split()
for S in s:
    print(S, end = " ")

# 3. 
c = int(input("테스트 케이스마다 입력 값을 그래도 출력하세요."))
for C in range(1, c+1):
    print(C)

# 4.
Ns = list(map(int, input("2개 이상의 정수를 출력하세요.").split()))
for NS in Ns: 
    print(NS)

#5
a, b = map(int, input("2개의 정수를 출려하세요.").split())
print(a, b)

# 6
s = input("단어를 구분해서 출력하세요").split()
for S in s:
    print(S)

# #7
c = int(input("테스트 케이스마다 입력값을 그대로 출력하세요"))
n = 0
for C in range(1, c+1):
    li = []
    for R in range(1+(3*n), 4+(3*n)):
        li.append(R)
    print(*li, sep=",")     # [] 없이 출력 for 구문으로 대체 가능

    n += 1
    
    
    

# 8
c = int(input("테스트 케이스마다 입력값을 그대로 출력하세요"))
for C in range(1, c+1):
    n = list(map(int, input().split()))
    for N in n:
        print(N, end = " ")

