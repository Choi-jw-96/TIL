#17608
import sys
stick = int(input())
stick_list = []
cnt = 0

for _ in range(stick):
    stick_list.append(int(sys.stdin.readline()))

stick_h = 0

# reversed와 [::-1]은 시간을 너무 먹어서 for문으로 인덱스를 반대로 걸음
for i in range(stick-1 , -1, -1):
    # 스틱 인덱스가 크가면 하이를 바꾸고 +1씩 한다
    if stick_list[i] > stick_h:
        stick_h = stick_list[i]
        cnt += 1

print(cnt)

"""
용진님
import sys
sys.stdin = open('input.txt','r')

num = int(input())
d = dict()
a = []
temp = 0
for i in range(1,num+1):
    d[i] = int(input())

for x in range(num,0,-1):
    temp = max(d[x],temp)
    if d[x] > temp : 
        a.append(d[x])
    else:
        a.append(temp)

b = list(set(a))
print(len(b))
"""
    


#7568
people = int(input())
people_list = []

for _ in range(people):
    x = list(map(int, input().split()))
    people_list.append(x)

h = []
# 순서를 지켜줄 인덱스
for i in range(people):
    cnt = 0

    # 비교할 인덱스
    for j in range(people):
        # 자기보다 등치가 큰사람 있다면 += 1
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            cnt += 1
    h.append(cnt + 1)


print(*h)



#1063
chess = [[False] * 8 for _ in range(8)]
delta = {"R" : (0, 1), "L" : (0, -1), "B" : (1, 0), "T" : (-1, 0),
"RT" : (-1, 1), "LT" : (-1, -1), "RB" : (1, 1), "LB" : (1, -1)}

king, stone, n = map(str ,input().split())

# 이중리스트 안에 넣어준다
chess[8 -int(king[1:])][ord(king[:1])-65] = "king"
chess[8 -int(stone[1:])][ord(stone[:1])-65] = "stone"

# 이동 명령어를 반는 for
for _ in range(int(n)):
    move = input()
    # 델타에서 입력같을 가져옴
    for key, value in delta.items():
        if move == key:
            # 아래로 내려갔을때 반복을 막기위한 stop(마지막 행이었을 경우를 위해 여기서 초기화)
            stop = ""
            for i in range(8):
                if stop == "break":
                    stop = ""
                    break
                for j in range(8):
                    # 채스판을 벗어나면 pass
                    try:
                        # 킹이면서 양수일때
                        if chess[i][j] == "king" and i + value[0] >= 0 and j + value[1] >= 0:
                            # 넘거가는 곳에 스톤이 있다면
                            if chess[i + value[0]][j + value[1]] == "stone":
                                # 스톤이 밀리고도 체스판 안에 있다면
                                if  i + value[0] + value[0] >= 0 and j + value[1] + value[1] >= 0:
                                    chess[i + value[0] + value[0]][j +  value[1] + value[1]] = "stone"                               
                                    chess[i][j] = "False"
                                    chess[i + value[0]][j + value[1]] = "king"
                                    stop = "break"
                                    break

                                #없다면 그냥 멈춤
                                else:
                                    stop = "break"
                                    break
                            # 스톤을 밀지 않는다면
                            else:
                                chess[i][j] = "False"
                                chess[i + value[0]][j + value[1]] = "king"
                                stop = "break"

                                break               
                    except:
                            pass
                

 
for i in range(8):
    for j in range(8):
        if chess[i][j] == "king":
            k_i = i
            k_j = j
        elif chess[i][j] == "stone":
            s_i = i
            s_j = j

print(chr(65 + k_j) + str(8 - k_i))
print(chr(65 + s_j) + str(8 - s_i))

"""
# 다른 답안
king, stone, N = input().split()

k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))

dire = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

for _ in range(int(N)):
    m = input()
    k_nx = k[0] + dire[m][0]
    k_ny = k[1] + dire[m][1]
    if 0 < k_nx <= 8 and 0 < k_ny <= 8:
        if k_nx == s[0] and k_ny == s[1]:
            s_nx = s[0] + dire[m][0]
            s_ny = s[1] + dire[m][1]
            if 0 < s_nx <= 8 and 0 < s_ny <= 8:
                k = [k_nx, k_ny]
                s = [s_nx, s_ny]
        else:
            k = [k_nx, k_ny]

print(f'{chr(k[0] + 64)}{k[1]}', f'{chr(s[0] + 64)}{s[1]}', sep = '\n')
"""