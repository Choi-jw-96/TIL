#5431
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    not_input = []

    for num in range(1, N + 1):
        # 숙제를 내지 않은 번호를 찾아 append한다
        if num not in nums:
            not_input.append(num)
    
    print(f"#{t}", *sorted(not_input))



#2001
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 이중 리스트로 받는다
    fly = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    sum = 0

    # 행 기준으로 0 ~ n-m+1까지 반복되게
    for m in range(N - M + 1 ):
        # 열이 돌아가게
        for n in range(N - M + 1):
            # 이렇게 할 필요없이 파리테를 만들어서 지정할 수 있었을까?(과제)
            sum_list.append(sum)
            sum = 0
            # 행을 파리채 크기만큼 돌려줘
            for i in range(m, m + M):
                # 열을 파리채 크기만큼 돌려줘
                for j in range(n, n + M):
                    sum += fly[i][j]

    print(f"#{t} {max(sum_list)}")



#1983
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T +1):
    stu, who = map(int, input().split())
    # 높은 순서대로 점수 리스트화
    t_score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    s_total = []

    s_sco = [list( map(int, input().split())) for _ in range(stu)]

    for S in s_sco:
        # 모든 학생들의 점수를 리스트에 넣는다
        s_total.append(S[0] * .35 + S[1] * .45 + S[2] * .2)

        # 찾고싶은 학생의 점수를 찾아 놓는다
        if S == s_sco[who - 1]:
            who_sco = S[0] * .35 + S[1] * .45 + S[2] * .2
    
    # 오름차순 정렬
    s_total = sorted(s_total, reverse = True)

    # 찾는 학생의 순위를 찾는다
    for i in range(1, stu + 1):
        if s_total[i-1] == who_sco:
            # 학생의 순위로 받을 수 있는 점수를 구한다
            for n in range(1, 11):
                if (stu / 10) * n >= i:
                    print(f"#{t} {t_score[n-1]}")
                    break




#1979
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    word_puzzle = [list(map(int, input().split())) for _ in range(N)]
    row = 0
    column = 0

    # 행우선
    for i in range(N):
        cnt = 0
        cnt_list = []
        for j in range(N):
            # 해당 좌표가 비어있다면 cnt += 1
            if word_puzzle[i][j] == 1:
                cnt += 1
            else:
                # 지끔까지 쌓아온 cnt 저장
                cnt_list.append(cnt)
                cnt = 0

            # 마지막까지 돌았으면 cnt 저장            
            if j == N - 1:
                cnt_list.append(cnt)

        # cnt가 지정 칸수와 같다면 낱말을 끼울수 있다
        if K in cnt_list:
            # 같은 라인에 2개 이상 있을 수도 있으니 count 사용
            row += cnt_list.count(K)
    
    # 열 우선
    for i in range(N):
        cnt = 0
        cnt_list = []
        for j in range(N):
            if word_puzzle[j][i] == 1:
                cnt += 1

            else:
                cnt_list.append(cnt)
                cnt = 0
            
            if j == N - 1:
                cnt_list.append(cnt)
    
        if K in cnt_list:
            column += cnt_list.count(K)


    print(f"#{t} {row + column}")



#1225
# deque를 사용해서 pop(0)를 사용하지 않게함
from collections import deque

while True:
    t = int(input())
    nums = list(map(int, input().split()))
    nums = deque(nums)
    n = 0
    # nums[7] == 0이 아니라면 반복해
    while nums[7] != 0:
        # 반복 할 때마다 5가 되기 전까지 n을 1씩 증가
        n += 1
        if nums[0]-n > 0:
            nums.append(nums[0]-n)
        # 결과가 음수라면 nums[7]에 0을 넣어
        else:
            nums.append(0)
        # if와 상관없이 pop(0)를 지워줘    
        nums.popleft()

        if n == 5:
            n = 0

    print(f'#{t}', *nums)
    if t == 10:
        break
        


#1218
t = 0
while t < 10:
    t += 1
    num = int(input())
    pair = str(input())
    # 서로 짝이 갯수가 안맞나 봄
    # ] [ 경우는 찾을 수 없지 않은까 (과제)
    if pair.count("(") == pair.count(")"):
        if pair.count("[") == pair.count("]"):
            if pair.count("{") == pair.count("}"):
                if pair.count("<") == pair.count(">"):
                    print(f"#{t} 1")
                else:
                    print(f"#{t} 0")
            else:
                print(f"#{t} 0")
        else:
            print(f"#{t} 0")
    else:
        print(f"#{t} 0")

