# 비교연산자

a = 1
b = 1
print(a < b) # False


a = bool("")
b= False
print(a==b) #  True


# 비교연산자 + 조건문

a = 1
result = ""

if a == 1:
    result = True
else:
    result = False

print(result) # True


a = 90

if a== 90:
    a = a + 10

elif a == 100:
    a = a + 10

elif a == 110:
    a += 10

else:
    a += 10

a = a + 10

print(a) # 110


#  리스트 + 반복문

string = "hello world!"

for element in string:
    print(element)

"""
예측을 작성하세요
h
e
l
l
o

w
o
t
l
d
!
"""


list_varialbe = [0, 1, 2, 3, 4, 5, 6]

for element in list_varialbe:
    print(element, end="")

"""
예측을 작성하세요
0123456
"""


# range + 반복문

n = 10

for element in range(-n, n):
    print(element, end = "")

"""
-10-9-8-7-6-5-4-3-2-10123456789
"""


n = 10

for element in range(1, n + 1, 3):
    print(element, end = " ")

"""
1 4 7 10
"""


# list + 반복문

list_variable = [6, 5, 4, 3, 2, 1, 0]

for index, element in enumerate(list_variable):
    print(index, element)

"""
(0, 6)
(1, 5)
(2, 4)
(3, 3)
(4, 2)
(5, 1)
(6, 0)
"""


# 조건문 + range + 반복문

n = 10

for element in range(n, -n, -1):
    print(element, end = "")
    if n < 0:
        break

"""
109876543210
"""
"""
109876543210-1-2-3-4-5-6-7-8-9
"""

list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue

    print(element, end = "")

"""
351921
"""


# range + 중첩반복문

N = 3
M = 4

for n in range(N):
    for m in range(M):
        print(f"{n}, {m}")

"""
0
1
2
,
 
0
1
2
3
"""
"""
0, 0
0, 1
0, 2
0, 3
1, 0
1, 1
1, 2
1, 3
2, 0
2, 1
2, 2
2, 3
"""