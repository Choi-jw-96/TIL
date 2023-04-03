#9498
score = int(input())

if score < 60:
    print("F")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A") 


#9093
t = int(input())

for T in range(t):
    s = list(map(str, input().split()))
    for S in s:
        S = S[::-1]
        print(S, end = " ")


#11721
s = input()
n = len(s) // 10

for N in range(n+1):
    print(s[(N*10):(N*10)+10])


#2947
nums = list(map(int, input().split()))

while nums != sorted(nums):
    for i in range(4):  # 5[4]번째 숫자는 비교할 필요 없으니 4[3]번째 숫자까지 범위지정
        if nums[i] > nums[i+1]:
            num = nums[i]   # num에 i의 숫자를 저장
            nums.pop(i)     # i를 지운다
            nums.insert(i+1, num)   # num을 i+1에 다시 넣는다
            # nums[i], nums[i+1] = nums[i+1], nums[i] 한줄로 대체 가능
            print(*nums)    # if안에 들어온 것만 print해
        


