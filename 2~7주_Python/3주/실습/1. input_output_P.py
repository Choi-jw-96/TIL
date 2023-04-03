# 2 정수 1개
number = int(input())
print(number)



# 2 공백을 포함한 정수 2개
num1, num2 = map(int, input().split())
print(num1, num2)



# 3 공백을 포함한 정수 여러개
numbers = list(map(int,input().split()))
for number in numbers:
    print(number, end = " ")



# 4. 문자열 입력
word = list(map(str, input().split()))
for W in word:
    print(W, end = " ")



# 5 공백을 포함한 정수 여러개
num1, num2, num3, num4, num5 = map(int,input().split())
print(num1, num2, num3, num4, num5)



# 6
num1, num2 = map(int, input().split())
print(num1, num2)



# 7
word = list(map(str, input().split()))
for W in word:
    print(W, end = " ")



# 8 
num = list(map(int, input().split()))
for N in num:
    print(N, end = " ")



# 9
num = list(map(int, input().split()))
for N in num:
    print(N, end = " ")