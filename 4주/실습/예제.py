#10818
cnt = int(input())
nums = list(map(int, input().split()))
mini = min(nums)
ma = max(nums)
print(mini, ma)


#11720
cnt = int(input())
nums = input()
sum = 0
for num in nums:
    sum += int(num)
print(sum)


#2750
cnt = int(input())
nums = []
for C in range(cnt):
    num = int(input())
    nums.append(num)
for S_num in sorted(nums):
    print(S_num)


# 2562
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())
num9 = int(input())
nums = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
M = 0 

for n in range(9):
    if M < nums[n]:
        M = nums[n]
print(M)
print(nums.index(M) + 1)

