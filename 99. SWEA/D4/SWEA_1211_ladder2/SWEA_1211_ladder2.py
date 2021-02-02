import sys; sys.stdin = open("input_1211.txt", "r")

dy = [0, 0, 1]
dx = [-1, 1, 0]

def search(y, x):
    if y == 99:
        return visit[y][x]
    for i in range(3):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < 100 and 0 <= tx < 100 and visit[ty][tx] == 0 and arr[ty][tx] == 1:
            visit[ty][tx] = visit[y][x] + 1
            return search(ty, tx)

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)
    cnt = 1000
    ans = 100
    for i in range(len(start)):
        visit = [[0] * 100 for _ in range(100)]
        visit[0][start[i]] = 1
        num = search(0, start[i])
        if cnt > num:
            cnt = num
            ans = start[i]
    print('#{} {}'.format(tc, ans))