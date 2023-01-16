def cube(a):
    return a ** 3
print(cube(2))
print(cube(100))

def add(*numbers):              # * 인수를 무한으로 받음
    result = 0
    for n in numbers:
        result += n
    return result
print(add(1, 2, 3, 10, 23))


def movie(**kwargs):           # **은 딕셔너리
    return kwargs

print(movie(name = "더 글로리", writer = "김은숙" ))
print(kwargs)

# open('readme', 'r', encoding = 'utf8') => 3번째는 버퍼링이라 인코딩을 정의해서 작성해야한다



""""""
#globla scope
a = 10

#local scope
def foo():
    b = 10
    print(b)    # 10
foo()
print(b)    # error



a = 5

def foo():
    print(a)    # 5 local 안에 없어서 global을 가지고 옴.(좋은 함수는 아님)
foo()

def boo():
    global a    # global에도 3이라고 정의하라
    a = 3   # local 안에 있으니까
    print(a)    # 3
bool
print(a)    # 3 global 3이라는 정의를 내려서
