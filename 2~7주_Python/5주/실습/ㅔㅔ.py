s_n, n_n = map(int, input().split())
S_list = []
N_list = []

for _ in range(s_n):
    S = input()
    S_list.append(S)

for __ in range(n_n):
    N = input()
    if N in S_list:
        N_list.append(N)

print(len(N_list))