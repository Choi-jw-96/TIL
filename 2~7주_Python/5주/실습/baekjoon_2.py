#10817
import heapq
A, B, C = map(int, input().split())
heap = []
heapq.heappush(heap, A)
heapq.heappush(heap, B)
heapq.heappush(heap, C)

heapq.heappop(heap)     # 제일 앞에 있는(최소값) 값을 지워라
print(heap[0])



#20001
start = input()

q = 0       # 변수 선언

if start == "고무오리 디버깅 시작":
    while True:
        N = input()
        
        if N == "고무오리 디버깅 끝":
            break
        else:
            if N == "고무오리":
                if q == 0:
                    q += 2
                else:
                    q -= 1
            elif N == "문제":
                q += 1
    if q == 0:
        print("고무오리야 사랑해")
    else:
        print("힝구")



#1269
import sys

a, b = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

print(len(set(A)^set(B)))



#3052
#if
remainder = []
for t in range(10):
    num = int(input()) % 42
    if num not in remainder:
        remainder.append(num)
print(len(remainder))

#set
remainder = []
for t in range(10):
    num = int(input()) % 42
    remainder.append(num)
print(len(set(remainder)))



#1181
Ns = []
a = int(input())
for _ in range(a):
    Ns.append(input())

Ns = set(Ns)
Ns = sorted(list(Ns))   # 오름차순 먼져 정렬
Ns = sorted(Ns, key= len)   # 글자 수대로 정렬

print(*Ns, sep = "\n")

# set 하면 type가 dict 이고 sorted 하니까 type가 list로 바뀌

실패코드
import heapq
Ns = []
NS = []
a = int(input())
for _ in range(a):
    n =input()
    if n not in Ns:
        Ns.append(n)

Ns = sorted(Ns)

for __ in Ns:
    heapq.heappush(NS, (len(__), __))
    print(NS)



#11286
import heapq, sys
heap = []
N = int(input())

for n in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:    # 비어있지 않으면
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(heap, (abs(x),x))
