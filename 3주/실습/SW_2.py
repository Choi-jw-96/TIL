#1.  
title = input().upper()     # 가로 주의
print(title)



#2. 2025
n = int(input())
t = 0
for N in range(1, n + 1):
    t += N
print(t)




#3. 1936
A, B = map(int, input().split())
if A > B:
    if A != B * 3:
        print("A")
    else:
        print("B")
elif B > A:
    if B != A *3:
        print("B")
    else:
        print("A")



#4. 2027
print("#++++")
print("+#+++")
print("++#++")
print("+++#+")
print("++++#")




#5. 2058
a = input()     # int는 for 안됨
t = 0
for A in a:
    t += int(A)
print(t)


"""
성준님
for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else :
            print('+', end='')
    print()
"""


#6. 2019
a = int(input())
result = 1
list = []  
for A in range(1, a + 2):
    list = result
    result *= 2

    print(result, end =" ")



"""
세호님
n = int(input())

for i in range(n+1):
    print(2**i, end=' ')
    """