#2576
num_list = []
for n in range(7):
    num = int(input())
    if num % 2 == 1:
        num_list.append(num)
if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)

#2576 딕셔너리 풀이
num_dict = {}

for n in range(7):
    num = int(input())
    if num % 2 ==1:
        num_dict[num] = num_dict.get(num, )

print(sum(num_dict.keys()))
print(min(num_dict.keys()))



#10822
total = 0
S = input()
S = S.replace(",", " ").split()
for s in S:
    total += int(s)
print(total)


#딕서너리 
n_dict = {}
S = list(map(int, input().split(",")))
for s in S:
    n_dict[s] = n_dict.get(s, )
print(sum(n_dict.keys()))



#2754
score_dict = {"A+" : 4.3, "A0" : 4.0, "A-" : 3.7,

"B+" : 3.3, "B0" : 3.0, "B-": 2.7,

"C+" : 2.3, "C0" : 2.0, "C-" : 1.7,

"D+" : 1.3, "D0": 1.0, "D-" : 0.7,

"F" : 0.0}

my_score = input()

for key, value in score_dict.items():     ## 메서드 () 놓치지 말기!
    if my_score == key:
        print(value)

# 현석님 코드 print(dict[input()]) 한줄로 가능


#5622
tel = {2 : "ABC", 3 : "DEF", 4 : "GHI", 5 : "JKL", 
6 : "MNO", 7 : "PQRS", 8 : "TUV", 9 : "WXYZ"}

phone = input()
time = 0

for P in phone:
    for num, alpha in tel.items():
        if P in alpha:
            time += num + 1
            break
print(time)


#2577
nums_dict = {}
A = int(input())
B = int(input())
C = int(input())

for n in range(10):
    nums_dict[n] = nums_dict.get(n, 0)

for key, value in nums_dict.items():
    for abc in str(A*B*C):
        if int(abc) == key:
            value += 1
    print(value)


#7785 현석님 코드를 보고 다시 만듬
office = {}

T = int(input())

for t in range(T):
    human, work = map(str, input().split())
    office[human] = work
for key in sorted(office.keys(), reverse= True):        #key만을 가지고 해야지 시간초가가 안남
    if office[key] == "enter":
        print(key)  



#현석님 코드

company = {}
for t in range(int(input())):
    Key, Value = input().split()
    if Value == 'enter':
        company[Key] = True
    else:
        del(company[Key])

for Key in sorted(company.keys(), reverse=True):
    print(Key)


# 시간초과 1
office = {"enter" : [], "leave" : []}

T = int(input())

for t in range(T):
    human, work = map(str, input().split())
    for off, hum in office.items():
        if human in office["enter"]:
            hum.remove(human)
        if human in office["leave"]:
            hum.remove(human)
        if work == off:
            hum.append(human)
            break
    
        
print(*sorted(office["enter"], reverse=True), sep = "\n")
# 역순 잘보기

# 시간 초과 2
office = {}
in_office = []

T = int(input())

for t in range(T):
    human, work = map(str, input().split())
    office[human] = work


for hum, on_off in office.items():
    if on_off == "enter": 
        in_office.append(hum)
print(*sorted(in_office, reverse=True), sep="\n")




