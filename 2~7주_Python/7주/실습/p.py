graph=[[1,2],[0,3,4],[0,4,5],[1],[1,2,6],[2],[4]]
visited=[False]*7
def dfs(start):
    stack=[start]
    visited[start]=True
    while stack:
        cur=stack.pop()
        for adj in graph[cur]:
            if not visited [adj]:
                print(adj)  #방문순서 확인하기위해 사용
                visited[adj]=True
                stack.append(adj)
dfs(0)



