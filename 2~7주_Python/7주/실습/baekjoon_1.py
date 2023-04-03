#10769
message = input()

happy = message.count(":-)")
sad = message.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")



#2455
passenger = 0
passenger_list = []

for _ in range(4):
    out_p, in_p = map(int, input().split())
    passenger += in_p - out_p
    passenger_list.append(passenger)

print(max(passenger_list))



#2606
desktop = int(input())
link = int(input())

# 순서를 맞추려면 desktop + 1
graph = [ [] for _ in range(desktop + 1)]

for _ in range(link):
    a, b = map(int, input().split())
    #각각 넣어줘
    graph[a].append(b)
    graph[b].append(a)

visited= [False] * (desktop + 1)

def dfs(start):
    stack=[start]
    visited[start] = True
    
    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

#1부터 시작하자
dfs(1)

cnt = 0

for _ in visited:
    # 바뀐 부분만 구해줘
    if _ == True:
        cnt += 1
print(cnt - 1)



# #현석님
# def dfs(start):
#     global total # 글로벌에 토달을 가져와
#     visited[start] = 1 # True
#     for i in graph[start]:
#         if visited[i] == 0: # 방문하지 않은 곳이 있다면?
#             dfs(i) # 방문해봐라
#             total += 1
              
# n = int(input()) # 컴퓨터 수
# m = int(input()) # 컴퓨터 쌍의 수
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)


# visited = [0]*(n+1) # 방문 체크
# total = 0 
# dfs(1) # 1부터?
# print(total)



#인접 행렬 풀이
N = int(input()) # 노드 수

M = int(input()) # 간선 수

# 인접 행렬 만들기
graph = []
for _ in range(N + 1):
    temp = [0] * N + 1
    graph.append(temp)

# 정점의 쌍 입력
for _ in range(M):
    node1, node2 = list(map(int, input().split()))

    # 간선 표현
    graph[node1][node2] = 1
    graph[node2][node1] = 1

# 시작점
start = 1

# 스텍 방문 변수 넣고 방문 표시
stack = [start]
visit = set()
visit.add(start)

while stack:
    current_node = stack.pop()

    for index_node in range(N+1):
        # print(f'확인 정점 : {index_node}')
        # print(f'간선 여부 : {graph[current_node][index_node]}')
        # 인접해 있다면
        if graph[current_node][index_node] == 1:
            # 방문표시
            if index_node not in visit:
                visit.add(index_node)








#4963 
def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    island[x][y] = 0
    for _ in range(8):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < h and 0 <= ny < w and island[x][y] == 1:
            dfs(nx, ny)

cnt = 0
while True:
    w, h = map(int, input().split())

    island = [[0] * w for _ in range(h)]
    
    for _ in range(h):
            island[_] = list(map(int, input().split()))

    for H in range(h):
        for W in range(w):
            if island[H][W] == 1:
                dfs(H, W)
                cnt += 1
                        

    if w == 0 and h ==0:
        break
