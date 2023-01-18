#2789
s = str(input())

for A in ["C", "A", "M", "B", "R", "I", "D", "G", "E"]:
    if s.find(A) == -1:
        pass
    else:
         s = s.replace(A,"")    # strip은 끝에있는 글자만 지워짐
print(s)


#2675
t = int(input())
for T in range(t):
    num, s = map(str, input().split())
    pint =""

    for S in s:
        S_ = S * int(num)
        pint += S_
    print(pint)



#10988
s = str(input())

if s == s[::-1]:
    print(1)
else:
    print(0)



#17249
teabo = str(input())
face = teabo.find("(^0^)")
L_rock = teabo.count("@", 0, face)
R_rock = teabo.count("@", face, len(teabo))
print(L_rock, R_rock)

 

#2941
s = str(input())
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

for ap in alpha:
    if s.count(ap) >= 1:
        cnt += s.count(ap)
s_c = len(s) - cnt
print(s_c)


#10809
S = str(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
# cnt = []

for abc in alpha:
    # cnt.append(S.find(abc))
#print(*cnt)
    print(S.find(abc), end = " ")

# ## 아스키 버전
# alpha = range(97, 123)

# for abc in alpha:
#     print(S.find(chr(abc)), end =" ")



