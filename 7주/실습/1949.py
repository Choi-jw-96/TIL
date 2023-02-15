# 땅을 파기 전까지 성공적인 코드를 완성했었지만 땅을 파고나서 애들이 중구난방으로 돌아다녀
# visited 없이 못하겠다는 것을 깨닫고 다시 코드는 짰다.
# 하면서 카운트를 따로 받았었는데 계속 더해져서 멘붕이 왔었다
# 결국 visited에 값을 넣으며 가기로 했다.
# 나올때 초기화가 곤란해 졌다.
# 초기화는 구글링을 해서 할 수 있었다
# 결국 마지막에는 코드를 보고 풀게 돼서 내게 실망했다.
import sys
sys.stdin = open("input.txt", "r")

# 상하좌우로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 함수
# 값을 가져올것
def dsf(I, J, K):
    # 글로벌에서 바꿔가면서 가져갈것
    global MaX, visited
    # 멀리 갈 수록 높아지게 설정
    MaX = max(MaX, visited[I][J])

    # 상하 좌우로 이동하면서 본다
    for im in range(4):
        mx = I + dx[im]
        my = J + dy[im]

        # 표 안에 있으면서 visited에서 이미 갔다는 표시가 없는곳
        if 0 <= mx < n and 0 <= my < n and visited[mx][my] == 0:
            # 그냥 갈 수 있는 경우(작은 경우)
            if mountain[I][J] > mountain[mx][my]:
                # 원래 있던 장소보다 1 더한다
                # 별도로 수를 넣었을때 초기화를 한번 더 넣어줘야해서 뺌
                visited[mx][my] = visited[I][J] + 1
                # 걸어간 곳에서 다시 함수 실행
                dsf(mx, my, K)

                # 갈림길에서 빠져나올때 visited에서 지나올 길을 0으로 초기화
                visited[mx][my] = 0
            
            else:
                # 큰 곳 중 땅을 파면 갈 수 있는곳
                if K != 0 and mountain[I][J] > mountain[mx][my] - K:
                    # 땅을 파기전에 돌아갈 때를 생각해서 파기전 땅을 저장
                    temp = mountain[mx][my]
                    # 지금있는 땅보다 -1만 더 판다
                    mountain[mx][my] = mountain[I][J] - 1
                    visited[mx][my] = visited[I][J] + 1
                    dsf(mx, my, 0)

                    # 갈림길에서 빠져나올때 판 땅을 돌려놓고 지나간 자리를 0으로 초기화 
                    mountain[mx][my] = temp
                    visited[mx][my] = 0



# 입력
T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    # 높은 봉우리 찾기
    maxi = []
    for N in mountain:
        maxi.append(max(N))
    start = max(maxi)

    # 가장 높은 곳을 찝하줄 값(for안에 들어가면 초기화가 돼서 안됨)
    MaX = 0
    # 산 중 가장 높은곳에서 시작(높은 곳은 중복)
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == start:
                visited[i][j] = 1
                dsf(i, j, k)
                # 함수에서 나오고 0으로 초기화
                visited[i][j] = 0

    print(f'#{t} {MaX}')

