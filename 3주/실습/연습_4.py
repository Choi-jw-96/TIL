





members = ['홍엽', '세정']
for i, member in enumerate(members):
    print(i, member)


list_a = []
for i in range(1, 4):
    a = i ** 3
    list_a.append(a)
print(list_a)

[i**3 for i in range(1,4)]



number = ['1', '2', '3']
# 숫자로 바꾸고 싶다면
n_numbers = list(map(int, number))      # map 형변환

number = [2, 1], [3. 1]
# 정렬 싶다면? [1, 2], [1, 3]
print(list(map(sorted, number)))


number = [2, 4]

def div_2(n):
    return n // 2
print(list(map(div_2, number)))
print(list(map(lambda n : n//2 , number)))      # 한번쓰고 다음엔 안 쓸라면 익명 함수



def g(x : int, y : int) -> int:
    return x + y
n = (1, 2)
g(n)





