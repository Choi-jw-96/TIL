# 1.리스트 + 반복문


list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)


for element in list_variable[2:]:  # : 슬라이스를 의미
    print(element, end = " ")

"""
2 3 4 5 7 8
"""

# 2.range + 반복문

for element in range(-2, 10, 2):
    print(element, end = " ")

"""
-2 0 2 4 6 8
"""


# 3. 조건문 + 반복문

a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a += 1

    if number % 3 == 0:
        b += 1
    if number % 4 == 0:
        c += 1
    if number % 5 == 0:
        d += 1
print(a, b, c, d)    # (5, 4, 3, 2)


# 4. 비교연산자 + 반복문
i = 0
while i <= 10:
    print(i)
    i += 1

"""
0
1
2
3
4
5
6
7
8
9
10
"""


# 5. 비교연산자 + 반복문
i = 0
while i <= 10:
    i += 1
    print(i)

"""
1
2
3
4
5
6
7
8
9
10
11
"""


# 6. 조건문 + 반복문

i = 0
while i <= 10:
    i += 2
    print(i)

"""
2
4
6
8
10
12
"""


# 7. 조건문 + 반복문
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break

"""
0
1
2
3
4
5
6
7
8
9
"""    # 10


# 8. 조건문 + 반복문
i = 0
while True:
    print(i)
    if i > 10:
        break
    i += 1

"""
0
1
2
3
4
5
6
7
8
9
10
"""    #11 ? => 10에서 print 되고 if에 들어가서 break


# 9. 함수
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable))    # 7


# 10. 함수
list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable))    # 21


# 11. 함수
list_variable = [3, 1 ,4, -3, 9, 7]
print(min(list_variable) - max(list_variable))    # -12 
