import sys; sys.stdin = open("input_1868.txt", "r")
from collections import deque

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def counting(y, x):
    for i in range(8):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < N and 0 <= tx < N and arr[ty][tx] == '*':
            return 1
    return 0

def search(y, x):
    Q = deque()
    Q.append((y, x))
    visit[y][x] = 1
    while Q:
        Y, X = Q.popleft()
        for i in range(8):
            ty = Y + dy[i]
            tx = X + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visit[ty][tx]:
                visit[ty][tx] = 1
                if arr[ty][tx] == 0:
                    Q.append((ty, tx))

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    zeroPoint = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                arr[i][j] = counting(i, j)
            if arr[i][j] == 0:
                zeroPoint.append((i, j))
    click = 0
    visit = [[0] * N for _ in range(N)]
    for r, c in zeroPoint:
        if visit[r][c]:
            continue
        search(r, c)
        click += 1
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and arr[i][j] != '*':
                click += 1
    print('#{} {}'.format(tc, click))


