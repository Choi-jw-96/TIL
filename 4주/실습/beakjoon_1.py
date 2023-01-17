#10039
# list.pop .append를 사용하면 리스트의 순서가 변경되어 원하는 값과 달리 나옴.
stu_1 = int(input())
stu_2 = int(input())
stu_3 = int(input())
stu_4 = int(input())
stu_5 = int(input())
stu_total = 0
stu_list = [stu_1, stu_2, stu_3, stu_4, stu_5]

for N in range(5):
    if stu_list[N] < 40:
        stu_total += 40
    else:
        stu_total += stu_list[N]

stu_avg = stu_total / len(stu_list)
print(int(stu_avg))



#10871
N, X = map(int, input().split())
Ns = list(map(int, input().split()))
S_Ns = []
for n in range(N):
    if Ns[n] < X:
        S_Ns.append(Ns[n])
print(*S_Ns)

"""N , X  = list(map(int,input().split()))
A = list(map(int,input().split()))

for n in A[:]:
    if n > X-1:
        A.remove(n)
    else:
        continue

print(*A)"""



#2480
Dice_1, Dice_2, Dice_3 = map(int, input().split())
D_list = [Dice_1, Dice_2, Dice_3]
mny = 0
if Dice_1 == Dice_2 == Dice_3:
    mny = 10000 + (Dice_1 * 1000)
elif Dice_1 != Dice_2 and Dice_1 != Dice_3 and Dice_2 != Dice_3:
# Dice_1 != Dice_2 != Dice_: 와는 다르다. 이 경우 1 != 2와 2 != 3만 비교된다.
    D = 0
    for N in range(3):
        if D < D_list[N]:
            D = D_list[N]
    mny = D * 100
else:
    if Dice_1 == Dice_2:
        mny = 1000 + (Dice_1 * 100)
    elif Dice_1 == Dice_3:
        mny = 1000 + (Dice_1 * 100)
    else:
        mny = 1000 + (Dice_2 * 100)
print(mny)

"""
Dices = list(map(int, input().split()))
for Dice in Dices:
    if 3 == Dices.count(Dice):
        print(10000 + (Dice* 1000))
        break
    elif 2 == Dices.count(Dice):
        print(1000 + (Dice * 100))
        break
    else:
        print(max(Dice)*100)
        break
"""




    
#10886
peo = int(input())
Peo = []
for P in range(peo):
    Peo.append(int(input()))
if Peo.count(1) > Peo.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")



#2506
Q = int(input())
q = list(map(int, input().split()))
sco = 0
sco_list= []
for N in range(Q):
    if q[N] == 1:
        sco += 1                # 점수를 누적 시켜
        sco_list.append(sco)    # 누적 점수를 리스트에 저장해
    else:
        sco = 0                 # 오답이면 누적 점수를 리셋 시켜
print(sum(sco_list))



#whil 경우
q = int(input())
nums = list(map(int, input().split()))
sco = 0
tal = 0
i = 0
while i < q:

    if nums[i] == 1:
        sco += 1                # 점수를 누적 시켜
        tal += sco 

    else:
        sco = 0
        
    i += 1  
print(tal)