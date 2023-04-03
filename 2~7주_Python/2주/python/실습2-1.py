# 문제 9

a = int(input("정수를 입력하세요 > "))
if a < 1:
    print(False)
else:
    for A in range(1, a):
        if A % 2 == 0:
            continue
        print(A)