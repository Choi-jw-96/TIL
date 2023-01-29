import heapq
# number = [0, 12345678, 1, 2, 0, 0, 0, 32]
# ctrl 방향키하면 커서가 많이 생긴다
number = int(input())
heap = []


for _ in range(number):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if heap:    #  비어있지 않으면!
            print(heapq.heappop(heap))
        else:
            print(0)

# list
cnt = 0
s_n, n_n = map(int, input().split())

for _ in range(s_n):
    S = input()

for __ in range(n_n):
    N = input()

for n in N:
    if n in S:
        cnt += 1
print(cnt)

# set
cnt = 0

S = set(S)

for n in N:
    if n in S:
        cnt += 1
print(cnt)

# set 연산
print(len(set(S) & set(N)))