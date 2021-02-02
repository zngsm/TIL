'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''
import sys; sys.stdin = open("14501.txt", "r")

def solve(idx, total):
    global max_income
    if T[idx:N] == [0] * (N - idx):
        if max_income < total:
            max_income = total
        return
    if (sum(P[idx:N]) + total) <= max_income:
        if max_income < total:
            max_income = total
        return
    if idx >= N - 1:
        if idx == N - 1 and P[idx]:
            total += P[idx]
        if max_income < total:
            max_income = total
        return

    for i in range(idx, N):
        if not visit[i] and T[i]:
            visit[i] = 1
            new_idx = i + T[i]
            new_total = total + P[i]
            solve(new_idx, new_total)
            visit[i] = 0
            solve(idx + 1, total)
            return


N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 퇴사 직전 아예 받을 수 없는 일들은 전부 0으로 바꿔주기
for i in range(N-1, -1, -1):
    atleast = N - i
    if T[i] > atleast:
        T[i] = 0
        P[i] = 0
max_income = 0
visit = [0] * N
solve(0, 0)

print(max_income)