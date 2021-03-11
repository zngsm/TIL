import sys; sys.stdin = open("input.txt", "r")

def solve(m, total):
    global ans
    if m >= 13:
        ans = min(ans, total)

    else:
        solve(m + 1, total + D * month[m])
        solve(m + 1, total + M)
        solve(m + 3, total + M3)

for tc in range(1, int(input()) + 1):
    D, M, M3, Y = list(map(int, input().split()))
    month = [0] + list(map(int ,input().split()))

    ans = Y
    solve(1, 0)

    print('#{} {}'.format(tc, ans))
