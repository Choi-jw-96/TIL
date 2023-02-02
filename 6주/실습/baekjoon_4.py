#1547
# 0번에 공이 들어있는 이중리스트를 만든다
cup = [[0], [], []]

M = int(input())

for _ in range(M):
    x, y = map(int, input().split())
    # x 인덱스 값을 _1에 저장하고 y->x, _1->x에 넣어서 위치를 바꾼다
    cup_1 = cup[x-1]
    cup[x-1] = cup[y-1]
    cup[y-1] = cup_1

# 비어있지 않은 리스트 인덱스를 찾고 +1한다.
for i in range(3):
    if cup[i] != []:        
        print(i+1)




#5576
#함수.ver(비슷하게 depeue도 가능)
w = [int(input()) for W in range(10)]
k = [int(input()) for K in range(10)]

# 내림차순으로 정렬
w = sorted(w, reverse = True)
k = sorted(k, reverse = True)

# 0~2까지 슬라이스한 합
print(sum(w[:3]), sum(k[:3]))


#for.ver
w = [int(input()) for W in range(10)]
k = [int(input()) for K in range(10)]

W_t = []
K_t = []

# 각 대학 중 인덱스 별로 젤 큰 수와 같은 3 점수를 모아서 새 리스트에 어팬드한다.
cnt_w = 0
for i in range(10):
    if w[i] == max(w[i:]):
        W_t.append(w[i])
        cnt_w += 1
        if cnt_w == 3:
            break

cnt_k = 0
for i in range(10):
    if k[i] == max(k[i:]):
        K_t.append(k[i])
        cnt_k += 1
        if cnt_k == 3:
            break

print(sum(W_t), sum(K_t))



#2846
n = int(input())
h = list(map(int, input().split()))
H = 0
H_list = []

# 서로 다른 인덱스끼리 비교하고 싶으니까 인덱스를 증가시킨다
for i in range(n):
    # 마지막에 i+1로 오류뜨는 것을 막기위해 설정해준다
    try:
        # 다음 인덱스끼리의 차이가 양수일때 차이만큰 H를 증가시킨다
        if h[i + 1] - h[i] > 0:
            H += h[i + 1] - h[i]
        
        else:
            # 음수라면 지금까지 모은 인덱스를 리스트에 넣은후 초기화
            H_list.append(H)
            H = 0

    # 마지막에 있던 H의 값을 리스트에 넣어준다.(마지막이 제일 클 경우 지정안하면 리스트에 안들어간다)
    except:
        H_list.append(H)

print(max(H_list))



#1251
i_list = []
S = input()

for s_1 in range(1, len(S)):
    for s_2 in range(s_1+1, len(S)):
        S_1 = S[:s_1]
        S_2 = S[s_1:s_2]
        S_3 = S[s_2:]
        i_list.append(S_1[::-1] + S_2[::-1] + S_3[::-1])

print(i_list)

print(sorted(i_list)[0])


#         if s_1 != s_2:
#             i += 1
#         else:
#             i_list.append(i)
#             i += 1
#             continue

#         if len(i_list) == 2:
#             break
#     if len(i_list) == 2:
#         break

# i_list = sorted(i_list)

# S_1 = S[ : i_list[0] + 1]
# S_2 = S[i_list[0] + 1 : i_list[1] + 1]
# S_3 = S[i_list[1] + 1 :]
# print(S_1[::-1], S_2[::-1], S_3[::-1], sep="")


 



