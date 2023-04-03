martix = []

for _ in range(10):
    martix.append([0]*10)



N = 4
M = 3

matrix = [[0] * M] * N
print(martix)
martix[0][0] = 1
print(martix)
[0,0,0], [0,0,0], [0,0,0], [0,0,0]
[1,0,0], [1,0,0], [1,0,0], [1,0,0]
# 주소값이 같아서 다 같이 바뀜
""""""
martix2 = [[0] * M for _ in range(N)]
print(martix2)
martix2[0][0] = 1
print(martix2)
[0,0,0], [0,0,0], [0,0,0], [0,0,0]
[1,0,0], [0,0,0], [0,0,0], [0,0,0]
# 주소값이 달라서 한개만 변경


mat = [list(map(int, input().split())) for _ in range(3)]
