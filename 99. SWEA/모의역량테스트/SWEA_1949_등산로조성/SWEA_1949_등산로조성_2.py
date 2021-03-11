import sys; sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def search(y, x, c):
    global is_change, ans

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty >= N or tx < 0 or tx >= N or visit[ty][tx] == 1:
            continue
        if arr[y][x] > arr[ty][tx]:
            visit[ty][tx] = 1
            search(ty, tx, c + 1)
            visit[ty][tx] = 0
        else:
            if not is_change:
                for k in range(1, K + 1):
                    if (arr[ty][tx] - k) < arr[y][x]:
                        arr[ty][tx] -= k
                        visit[ty][tx] = 1
                        is_change = True
                        search(ty, tx, c + 1)
                        arr[ty][tx] += k
                        visit[ty][tx] = 0
                        is_change = False

    else:
        ans = max(ans, c)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_num:
                max_num = arr[i][j]

    start = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_num:
                start.append((i, j))



    ans = 0
    for r, c in start:
        visit = [[0] * N for _ in range(N)]
        is_change = False
        visit[r][c] = 1
        search(r, c, 1)


    print('#{} {}'.format(tc, ans))
