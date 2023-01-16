my_list = ["서울", "서울", "대전", "광주", "서울", "대전", "부산", "부산"]
list_A = []
c = 0
for A in my_list:
    if A not in list_A:
        list_A.append(A)
print(list_A, len(list_A))
print(set(my_list))
print(len(set(my_list)))


""""""
text = "hello!"
a = text[::-1]
print(a)


""""""
drama = {'name' : '글로리', 'writer' : '김은숙'}
print(drama['director'])    # erorr
print(drama.get('director'))    # None
print(drama.get('director', 0))    # 0


""""""

my_list = ["서울", "서울", "대전", "광주", "서울", "대전", "부산", "부산"]
dict = {}

for list in my_list:
    # if list in dict:
    #     # dict.keys = my_list
    #     # dict[my_list] += 1
       
    # else:
    #     dict[my_list] = 1
    dict[my_list] = dict.get(list, 0) + 1
print(dict)