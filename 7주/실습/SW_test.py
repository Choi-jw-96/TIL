#11856
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    S = input()
    set_S = set(S)
    yes = 0
    if len(set_S) == 2:
        for n in set_S:
            if S.count(n) == 2:
                yes += 1
    
    if yes == 2:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")



#7465
import sys
sys.stdin = open("input.txt", "r")

def dfs(graph, n, visited):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

T = int(input())

for t in range(1, T + 1):
    hum, nei = map(int, input().split())
    town = [[] for _ in range(hum+1)]

    town_2 = [False] * (hum+1)
    town_2[0] = True

    for N in range(nei):
        hum_1, hum_2 = map(int, input().split())
        town[hum_1].append(hum_2)
        town[hum_2].append(hum_1)
    
    cnt = 0
    while False in town_2:
        cnt += 1
        dfs(town, town_2.index(False), town_2)
    
    print(f"#{t} {cnt}")




#4406
T = int(input())
for t in range(1, T + 1):
    word = input()

    for n in ["a", "e", "i", "o", "u"]:
        for __ in range(word.count(n)):
            word = word.replace(n, "")
    
    print(f"#{t} {word}")
    



#3499
for t in range(1, int(input()) + 1):
    card_n = int(input())
    card = list(map(str, input().split()))
        

    if card_n % 2 == 0:
        half = card_n // 2
    else:
        half = card_n // 2 + 1

    a = card[:half]
    b = card[half:]
    for i in range(half):
        card[i + i * 1] = a[i]
        try:
            card[i + 1 + i * 1] = b[i]
        except:
            pass       

    print(f'#{t}', *card)

    

#1949
import sys
sys.stdin = open("input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def road(graph, I, J, C):
    global M_cnt, visited
    M_cnt = max(M_cnt, visited[I][J])
    for i in range(4):
        x = I + dx[i]
        y = J + dy[i]
        if not(0<= x < N and 0 <= y < N) or visited[x][y]:
            continue

        if graph[I][J] > graph[x][y]:
            visited[x][y] = visited[i][j] + 1
            road(graph, x, y, C)
        
        elif C and graph[I][J] > graph[x][y] - chance:
            a = graph[x][y]
            graph[x][y] = graph[I][J] - 1
            visited[x][y] = visited[I][J] + 1
            road(graph, x, y, chance-1)
            visited[x][y] = 0
            graph[x][y] = a


T = int(input())
for t in range(1, T + 1):
    N, chance = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    start = 0
    for mx in mountain:
        if start < max(mx):
            start = max(mx)

    visited = [[0] * N for _ in range(N)]
    M_cnt = 0
    
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == start:                
                visited[i][j] = 1
                road(mountain, i, j, 1)
                visited[i][j] = 0

    print(f'#{t} {M_cnt}')



""""""


T = int(input())
cnt = 0

def road(graph, I, J, n, C, M):
    C += 1
    no = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        if 0<= I + dx[i] < n and 0<= J + dy[i] < n:
            if graph[I][J] > graph[I + dx[i]][J + dy[i]]: 
                road(graph, I + dx[i], J + dy[i], n, C, M)
            
            elif graph[I][J] <= graph[I + dx[i]][J + dy[i]]:
                if M != 0:
                    if graph[I][J] > graph[I + dx[i]][J + dy[i]] - M:
                        M = 0
                        road(graph, I + dx[i], J + dy[i], n, C, M)

    m_cnt.append(C)
                    
    return max(m_cnt)

for t in range(1, T + 1):
    N, chance = map(int, input().split())
    good_road = []
    mountain = [list(map(int, input().split())) for _ in range(N)]

    start = 0
    for mx in mountain:
        if start < max(mx):
            start = max(mx)

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == start:
                m_cnt = []
                good_road.append(road(mountain, i, j, N, cnt, chance))

    print(f'#{t} {max(good_road)}')



#1208
import sys
sys.stdin = open("input.txt", "r")
for t in range(1, 11):
    move = int(input())
    box = list(map(int, input().split()))

    for _ in range(move):
        box = sorted(box)

        box[0] += 1
        box[99] -= 1

    print(f"#{t} {max(box) - min(box)}")
        

