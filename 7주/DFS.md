# DFS(깊이 우선 탐색)

## 그래프 탐색 알고리즘

1. 깊이우선탐색(DFS)
스택을 이용하여 탐색(상위 → 하위로 탐색)
갈 수 있는 하위 정점까지 탐색 후 더이상 갈 곳이 없으면 상위로 올라가면서 순회

모든 정점 방문에 유리
코드 구현이 간단함


2. 너비우선탐색(BFS)
덱을 이용하여 탐색(상위부터 탐색)

최단 거리를 구하는 경우 유리


### DFS 동작 과정

```python
# 그래프는 인접행렬 or 인접리스트 방식으로 표현
graph=[[1,2], [0,3,4], [0,4,5], [1], [1,2,6], [2], [4]]

# 각 정점 방문 여부를 판별할 체크리스트 생겅
visited = [False] * 7
# visited = set()도 가능 중복을 없애주니까


def dfs(start):

    # 스택(후입선출) 이전 방문 여부를 저장(true라면 돌아가려고)
    stack=[start]   # stack = 0
    # 시작정점 방문 처리
    visited[start] = True # visited = [True, False, False, False, False, False, False]
    # visited = set() 이라면 visited.add(start)

    # 스택이 빌때까지
    while stack:    
        cur=stack.pop() # [0]

        for adj in graph[cur]:  #[1, 2]  

            if not visited [adj]:
            # visited = set() 이라면 adj not in visited
                print(adj)  #방문순서 확인하기위해 사용
                # 방문처리
                visited[adj]=True
                # 안들렸던 곳 스택에 넣기
                stack.append(adj)
dfs(0)

```


이차원 리스트 구현 연습
재귀, BFS
예
그리디/최단경로/정렬

