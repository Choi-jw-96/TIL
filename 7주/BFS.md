# BFS(너비 우선 탐색)
가까운 노드부터 우선 탐색하는 알고리즘

큐 자료구조를 이용

1. 시작 노드에 반복
2. 큐에서 노드를 꺼낸 뒤, 해당 노드의 인접 노드 중 `방문하지 않는 노드를 모두 큐에 삽입`하고 `방문` 처리(한꺼번에 하는게 특징)
3. 더이상 할 수 없을때까지 반복


## 최단거리를 알 때 사용!

## BFS동작 과정
```python
from collections
from collections import deque

def bfs(graph, start, visited):
    # 큐의 구현을 위해 deque 사용
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = "")
        #아직 방문하지 않은 인접한 원소를을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

bfs(graph, 1, visited)

```