a = int(input("숫자를 입력해 주세요 > "))

print(a + 10)


a = input("음식을 입력해주세요 > ")

print("좋아하는 음식 : ", a)


a = input("이름을 입력해주세요 > ")
b = int(input("태어난 년도를 입력해주세요 > ") )
c = str(int(2023) - b + 1)

# a = input("이름을 입력해주세요 > ")
# b = int(input("태어난 년도를 입력해주세요 > ") )
# c = int(2023) - b + 1

# print(f'저의 이름은 {a}이고, 올해 나이는 {c}세 입니다.')
# f를 사용하면 + 연산자 업이 숫자를 따로 분류해준다 

# print({}는 {}살이다. format(a, c))


print("저의 이름은 " + a + "이고, 올해 나이는 " + c + "세 입니다." )


a = input("첫 번째 문장을 입력해주세요 > ")
b = input("두 번째 문장을 입력해주세요 > ")
c = a + b

print(c)


a = int(input("숫자를 입력해 주세요 > "))

print(-1 * a)


a = int(input("첫 번째 숫자를 입력해 주세요 > "))
b = int(input("두 번째 숫자를 입력해 주세요 > "))

print("더하기 연산 :", a + b)
print("빼기 연산 :", a - b)
print("곱하기 연산 :", a * b)
print("몫 연산 :", int(a // b))
print("나머지 연산 :", a % b)


a = int(input("첫 번째 숫자를 입력해 주세요 > "))
b = int(input("두 번째 숫자를 입력해 주세요 > "))
c = int(input("세 번째 숫자를 입력해 주세요 > "))
d = (a + b + c) // 3

print(d)


list = []
a = int(input("첫 번째 숫자를 입력해 주세요 > "))
b = int(input("두 번째 숫자를 입력해 주세요 > "))
c = int(input("세 번째 숫자를 입력해 주세요 > "))
d = int(input("네 번째 숫자를 입력해 주세요 > "))
e = int(input("다섯 번째 숫자를 입력해 주세요 > "))

list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)

print(list)


a = input("문자열을 입력해주세요 > ")
b = int(input("숫자를 입력해주세요 > "))

print(a * b)


a = int(input("첫 번째 숫자를 입력해 주세요 > "))

print(a)

b = int(input("두 번째 숫자를 입력해 주세요 > "))

f = int(a + b)

print(f)

c = int(input("세 번째 숫자를 입력해 주세요 > "))

g = int(f + c)

print(g)

d = int(input("네 번째 숫자를 입력해 주세요 > "))

h = int(g + d)

print(h)

e = int(input("다섯 번째 숫자를 입력해 주세요 > "))

print(h + e)


# r = 0
# r += int(input("첫 번째 숫자를 입력해 주세요 > "))
# print(r)
# r += int(input("두 번째 숫자를 입력해 주세요 > "))
# print(r)
# r += int(input("세 번째 숫자를 입력해 주세요 > "))
# print(r)
# r += int(input("넷 번째 숫자를 입력해 주세요 > "))
# print(r)
# r += int(input("다섯 번째 숫자를 입력해 주세요 > "))
# print(r)