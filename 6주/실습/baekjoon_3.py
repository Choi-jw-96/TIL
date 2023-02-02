#2525
time, minute = map(int, input().split())
m_add = int(input())

if (minute + m_add) // 60 >= 1:
    time += (minute + m_add) // 60
    if time // 24 >= 1:       
        time = time % 24 

    minute = (minute + m_add) - ((minute + m_add) // 60) * 60

else:
    minute = minute + m_add
print(time, minute)

''''''

a,b = map(int, input().split())
c = int(input())
d = b + c

a += d//60
d %= 60

print(a % 24, d)




#2798
import sys
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, input().split()))

max_card = 0
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            add_card =  card[i] + card[j] + card[k]
            if add_card <= M and add_card > max_card :
                max_card = add_card


print(max_card)
    



#9076
## deque 풀이
from collections import deque
T = int(input())

for _ in range(T):
    score = list(map(int, input().split()))
    score = deque(sorted(score))
    score.pop()
    score.popleft()
    if score[2] - score[0] >= 4:
        print("KIN")
    else:
        print(sum(score))


##완전탐색
T = int(input())

for _ in range(T):
    score = list(map(int, input().split()))
    
    big = 0
    small = score[1]
    for i in range(5):
        for j in range(i+1, 5):
            if score[i] > score[j]:
                if big <= score[i]:
                    big = score[i]
                elif small >= score[j]:
                    small = score[j]
            else:
                if big <= score[j]:
                    big = score[j]
                elif small >= score[i]:
                    small = score[i]

    score.remove(big)
    score.remove(small)
    if max(score) - min(score) >= 4:
        print("KIN")
    else:
        print(sum(score))   





#1526
##두번째 속도를 올린 코드
N = int(input())

for n in reversed(range(4, N + 1)):
    ok = 0
    for i in range(len(str(n))):
        if str(n)[i] == "4" or str(n)[i] == "7":
            ok += 1
        else:
            break

    if ok == len(str(n)):
        print(n)
        break


##첫번째 코드
nums = []
N = int(input())

for n in range(4, N + 1):
    ok = 0
    for i in range(len(str(n))):
        if str(n)[i] == "4" or str(n)[i] == "7":
            ok += 1
        else:
            break

        if ok == len(str(n)):
            nums.append(n)
print(max(nums))





#1436
import sys
N = int(sys.stdin.readline())

movie = 666
cnt = 0

while True:
    if "666" not in str(movie):
        movie += 1
        continue
    else:
        cnt += 1
    
    if cnt == N:
        print(movie)
        break
    
    movie += 1
    
    


