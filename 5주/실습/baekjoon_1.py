#10101
triangle_1 = int(input())
triangle_2 = int(input())
triangle_3 = int(input())

if triangle_1 + triangle_2 + triangle_3 == 180:
    if triangle_1 and triangle_2 and  triangle_3 == 60:
        print("Equilateral")
    elif triangle_1 != triangle_2 and triangle_1 != triangle_3 and triangle_3 != triangle_2:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")



#2720
T = int(input())

for t in range(T):
    money = int(input())
    Quarter = money // 25
    Dime = (money - Quarter * 25) // 10
    Nickel = (money - (Quarter * 25 + Dime * 10)) // 5
    Penny = (money - (Quarter * 25 + Dime * 10 + Nickel * 5)) // 1
    print(Quarter, Dime, Nickel, Penny)

# # 현석, 계수님 코드
# money = [25, 10, 5, 1]
# for t in range(int(input())):
#     person = int(input())
#     lst = []
#     for i in money:
#         lst.append(person // i)
#         person = person % i
#     print(*lst)


#1453
online = []
people = int(input())

pc_num = list(map(int, input().split()))

for pc in pc_num:
    if pc not in online:
        online.append(pc)

print(len(pc_num) - len(online))



#10773
jangbu_list = []
T = int(input())

for t in range(T):
    num = int(input())
    if num == 0:
        jangbu_list.pop()   # 0이 나오면 list의 뒤부터 지워
    else:
        jangbu_list.append(num)
print(sum(jangbu_list))



#2161
pop_card = []
num = int(input())
card = list(range(1, num+1))

while len(card) > 1:    # while True를 쓰면 1넣어도 들어가지만 값이 안나와서 런타임 애러  
    pop_card.append(card[0])
    card.pop(0)
    
    card.append(card.pop(0))


print(*pop_card, *card)


#덱크 풀이
from collections import deque           # 앞뒤로 빼고 넣을 수 있음
num = int(input())
card = deque(range(1, num+1))           # list 대신 deque를 써서 적용

while len(card) > 1:
    print(card.popleft(), end = " ")    # ()밖부터 동시에 진행 즉,print하고 po[]

    card.append(card.popleft())         # append하고 pop

print(card[0])                          # 그냥 print(card) =  deque(6)







#9012
T = int(input())

for t in range(T):
    VPS = input()
    VPS_list = []

    for vps in VPS:
        if vps == "(":
            VPS_list.append(vps)

        else:
            if len(VPS_list) != 0:   # 없이 그냥하면 list가 비워있을때 오류가 뜸             
                if VPS_list[len(VPS_list) - 1] == "(":
                    VPS_list.pop()
            else:
                VPS_list.append(vps)

    
    if len(VPS_list) == 0:
        print("YES")
    else:
        print("NO")
# for 반복문이 break로 끝나지 않으면 else실행
