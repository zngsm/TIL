import sys; sys.stdin = open("input_5521.txt", "r")
from collections import deque
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    visit = [0] * (N + 1)
    Q = deque()
    Q.append(1)
    while Q:
        m = Q.popleft()
        for i in range(2, N+1):
            if visit[i] == 0 and arr[m][i] == 1:
                Q.append(i)
                visit[i] = visit[m] + 1
    ans = 0
    for v in visit:
        if 0< v < 3:
            ans += 1
    print('#{} {}'.format(tc, ans))