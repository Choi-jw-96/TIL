number1 = 1
number2 = number1 + 1
print(number1, number2)   #1, 2

#정답 1 2

number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2


print(number1, number2, number3, number4)   # 10 5 105 15

# 정답 10 5 105 15

string1 = "Hello"
string2 = string1
string3 = "World" + "!"


print(string2, "?", string3)   # Hello ? World!

# 정답 Hello ? World!

string = "Hello?"
n = 5


print(string * 5)   # Hello?Hello?Hello?Hello?Hello?

# 정답 Hello?Hello?Hello?Hello?Hello?

string = "adc hello def"
sub_string1 = string[4:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]


print(sub_string1)   # hello 
print(sub_string2)   # dc 
print(sub_string3)   # f

# 정답 hello / dc / f

number1 = 5
number2 = 10.0 + number1
number1 = 5
number3 = number1 * (number2 + 10)


print(number1, number2, number3)   # 5 15.0 125

# 정답 5 15.0 125.0

list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]


print(sub_list)   # 3

# 정답 3

list_variable = []
list_variable.append(1)
list_variable.append("a")
list_variable[0] = 0

print(list_variable)   # 0, a

# 정답 [0, 'a']

name = input("너의 이름은?")


print(name)   # 너의 이름은?최지원

# 정답
# 최지원

age =  int(input("너의 나이는?"))


print("올해 나이 : ", age)   # 올해 나이 : 28
print("내년 나이 : ", age + 1)   # 내년 나이 :29 

# 정답
# 올해 나이 :  28
# 내년 나이 :  29