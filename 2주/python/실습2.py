# 제어문

a = int(input("정수를 입력하세요 > "))

if a > 0:
    print("True")
else:
    print("False")



a = int(input("첫 번째 정수를 입력하세요 > "))
b = int(input("두 번째 정수를 입력하세요 > "))

if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(False)



a = int(input("정수를 입력하세요 > "))

if a < 10:
    if a > 1:
        print("True")
else:
    print("False")



a = int(input("정수를 입력하세요 > "))

if a % 2 == 0:
    if a > 0:
        print("True")
else:
    print("False")


a = int(input("정수를 입력하세요 > "))

if a > 100:
    print("에러")
elif a < 0:
    print("에러")
elif a >= 60:
    print("합격")
else:
    print("불합격")



a = input("문자열을 입력하세요 > ") 

# a_reverse = ""
# for A in a:
#     a_reverse += a

for A in reversed(a):
    print(A)



a = int(input("첫 번째 정수를 입력하세요 > "))
b = int(input("두 번째 정수를 입렵하세요 > "))

if a == b:
    print("False")
elif a < b:
    for A in sorted(range(a + 1, b)):
        print(A)
else:
    for B in sorted(range(b + 1, a)): 
        print(B)



a = int(input("첫 번째 정수를 입력하세요 > "))
b = int(input("두 번째 정수를 입렵하세요 > "))

if a == b:
    print("False")
elif a < b:
    for A in reversed(range(a + 1, b)):
    # for A in range(a + 1, b)[::-1]:
        print(A, end = " ")
else:
    for B in reversed(range(b + 1, a)): 
        print(B, end = " ")

# if a == b:
#     break




a = int(input("정수를 입력하세요 > "))

if a < 1:
    print(False)
else:
    for A in range(1, a, 2):
       print(A)


a = 2
b = 10

for A in range(a, b):
    for B in range(a, b):
        print(f"{A} X {B}")

