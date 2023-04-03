# 2441
n = int(input())

star = [[] * n for _ in range(n)]

for i in range(n):
    star[i] = [" " * i + "*" * (n - i)]
    print(*star[i])




#2592
# num을 받는다
nums = [int(input()) for _ in range(10)]

# num을 합하고 나눠 평균을 구한다
print(sum(nums) // len(nums))

# cnt를 비교할 c를 정의한다(초기화 하면 안됨)
c = 0
for i in nums:
    # 각 인덱스마다 초기화할 cnt를 정의한다
    cnt = 0
    for j in nums:
        # 같을 경우 cnt를 더해간다
        if i == j:
            cnt += 1
    if c < cnt:
        # cnt가 클 경우 c를 바꾸고 mode를 각 인덱스 값을 넣는다
        c = cnt
        mode = i

print(mode)

# 계수님!
numbers = [int(input()) for _ in range(10)]
print(sum(numbers)//len(numbers))
print(max(numbers,key = numbers.count)) 


# 용진님
from collections import Counter
lst = []
for i in range(10):
    a = int(input())
    lst.append(a)
counter = Counter(lst)
most = counter.most_common(2)

print(sum((lst))//10)
print(most[0][0])




#10798
# 문자열을 떨어뜨려 줘
strs = [list(input()) for _ in range(5)]

for i in range(15):
    for j in range(5):
        # 열의 수가 다르기 때문에 오류 상황을 정의
        try:
            print(strs[j][i], end = "")
        # 오류라면 패스해줘
        except:
            pass
        


#9455

T = int(input())

for _ in range(T):
    t_cnt = 0
    row, column = map(int, input().split())
    # 박스를 입렵받는다
    box = [list(map(int, input().split())) for __ in range(row)]

    # 열 우선 순회
    for i in range(column):       
        for j in range(row):
            # row에 -1을 하여 인덱스값을 만들고 -j를 하여 행의 맨 뒤값부터 읽는다 
            if box[row - 1 - j][i] == 1:
                cnt = 0
                n = 1
                # j가 0일땐 밑이 없으니까 우선적으로 오류제거를 위해 적어주고, +n을 하면서 내 아래있는 좌표가 1이면 넘어간다
                if j == 0 or box[row - 1 - j + n][i] == 1:
                    pass
                else:
                    # while로 현재 좌표가 1이면서 밑이 0일때 계속 내린다
                    while box[row - 1 - j + n][i] == 0:
                       box[row - 1 - j + n][i] = box[row - 2 - j + n][i]
                       box[row - 2 - j + n][i] = 0
                       cnt += 1
                       n += 1
                       # 행의 마지막까지 가면 멈춘다
                       if row - 1 - j + n > row - 1:
                           break
                    
                t_cnt += cnt 
    print(t_cnt) 


# 뒤집기를 이용한 코드(이게 더 짧음)
T = int(input())

for _ in range(T):
    t_cnt = 0
    row, column = map(int, input().split())
    box = [list(map(int, input().split())) for __ in range(row)]
    # 뒤집기 위해서 row열과 column행을 가질 임의의 박스를 만든다
    box2 = [[0] * row for ___ in range(column)]

    for i in range(column):       
        for j in range(row):
            # box2에 box의 행기준으로 들어올수 있도록 조정한다(오른쪽으로 90도 돌린다)
            box2[i][j] = box[row - 1 - j][i]

    cnt = 0

    # box2의 각 행(box의 열)들을 받고 각 인덱스별로 슬라이싱하여 오른쪽 정렬을 위해 움직여야할 0의 개수를 구한다
    for b in box2:
        for i in range(len(b)):
            try:
                if b[i] == 1:
                    cnt += b[:i].count(0)
            # 나오는 오류상황을 다 패스한다
            except:
                pass
    print(cnt)






# 실패코드
# 박스를 미는 것만 생각해서 cnt를 구하지 못했다.
T = int(input())

for _ in range(T):
    t_cnt = 0
    row, column = map(int, input().split())
    box = [list(map(int, input().split())) for __ in range(row)]
    # box2 = [[0] * column for ___ in range(row)]

    for i in range(column):
        cnt = 0
        for j in range(row):
            
            if box[row - j -1][i] == 1:
                n = -1
                if row - j -1 == 4:
                    pass
                elif box[j + n][i] == 0:
                    while box[j + n][i] == 1:
                        cnt += 1
                        n -= 1
                print(cnt)




#1652
N = int(input())      

room = [list(input()) for _ in range(N)]
row = 0
column = 0

#행 우선 순회
for i in range(N):
    cnt = 0
    for j in range(N):
        # .이 연속 2번 나오는 점을 센다. 여기서 ==2인 이유는 6칸이 비어도 3번 세지기 때문
        if room[i][j] == ".":
            cnt += 1
            if cnt == 2:
                row += 1
                
        else:
            cnt =0

#열 우선순회
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == ".":
            cnt += 1
            if cnt == 2:
                column += 1
                
        else:
            cnt =0
print(row, column)

        


