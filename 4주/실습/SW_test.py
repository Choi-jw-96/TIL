#14654
T = int(input())

for t in range(1, T+1):
    card = input()      # len을 위해 str로 받았다.
    if "-" in card:     # -를 뺀다
        card = card.replace("-", "")
    if len(card) == 16:
        if int(card[0:1]) in [3, 4, 5, 6, 9]:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        print(f'#{t} 0')


#14649
# T = [15 int], [홀](초기화),  [짝](초기화), add,  N
# 15 int의 홀 짝을 나누고 각 리스트에 묶는다(for len() in..: if % 2 == 0:)
# 홀에 짝의 합을 더해
# 나온 값이 10의 단위가 아니면 알맞는 N을 구한다
T = int(input())
add= 0 
N = 0

for t in range(1, T+1):
    odd = []
    even = []
    card = list(map(int, input().split()))    
    
    for i in range(1, 16):

        if len(card[0:i]) % 2 == 1:
            odd.append(card[i-1])
        else:
            even.append(card[i-1])

    add = sum(odd * 2) + sum(even)

    if add % 10 != 0:
        N = 10 - add % 10
    else:
        N = 0
    print(f'#{t} {N}')



#10804
# T, 문자열, 리스트(초기화)
# 문자열을 [::-1]
# replace를 쓰면 계속 변경이 될것 같으니 for로 따로 봐야 할 것같은 느낌
# for에 if문을 넣어서 알맞게 변경

T = int(input())
for t in range(1, T+1):
    s_list = []
    
    S = input()[::-1]   
    for s in S:
        if s == "b":
            s_list.append("d")
        elif s == "d":
            s_list.append("b")
        elif s == "p":
            s_list.append("q")
        else:
            s_list.append("p")

    print(f'#{t} ', end = "")
    print(*s_list, sep = "")
    

#10505
# T, 사람, 소득, 평균, 저소득(초기화)
# 평균보다 작은 사람구함

T = int(input())

for t in range(1, T+1):
    low_pay = 0
    peope = int(input())
    pay = list(map(int, input().split()))
    avg = sum(pay) // peope
    
    for P in pay:
        if P <= avg:
            low_pay += 1
    
    print(f'#{t} {low_pay}')


#3456
# T, 변 3개, 구할 변
# for.. if 변 1개.count = 홀(3=정사각형, 1=직사각형)/짝(직사각형 = 1개인 변을 찾자)

T = int(input())
N = 0

for t in range(1, T+1):
    square = list(map(int, input().split()))
    for n in square:
        if square.count(n) % 2 == 1:
            N = n
            break
    print(f'#{t} {N}')


#1204
# T, dict, 점수
# 점수를 받고 if 같은수가 없으면 딕셔너리에 점수 : 1 있으면 +1
# valus가 제일 큰 수는?

T = int(input())

for t in range(1, T+1):
    num = int(input())
    score_dict = {}
    scores = list(map(int, input().split()))
    
    for score in scores:
        if score not in score_dict:
            score_dict[score] = 1
        else:
            score_dict[score] += 1

    many = max(score_dict.items(), key = lambda x: x[1])
    # 더 쉽고 좋은 방법이 있을까? max(score_dict.value())가 안됐다.
    # 어제 비슷한 방식으로 풀었던 것 같은데 왜일까?
    
    print(f'#{t} {many[0]}')


# # 현석님
# from collections import Counter

# for t in range(1, int(input())+1):
#     n = int(input())
#     a = list(map(int, input().split()))
#     counter = Counter(a)
#     most_num = counter.most_common()[0][0]
#     print(f'#{t} {str(most_num)}')
