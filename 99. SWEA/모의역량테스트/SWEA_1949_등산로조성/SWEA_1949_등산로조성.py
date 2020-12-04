import sys; sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, cnt):
    global is_change, ans
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty >= N or tx < 0 or tx >= N or visit[ty][tx]:
            continue
        if arr[ty][tx] < arr[y][x]:
            visit[ty][tx] = True
            dfs(ty, tx, cnt + 1)
            visit[ty][tx] = False
        else:
            if is_change:
                for k in range(1, K + 1): ## K를 무조건 빼는게 아닌, K 범위 내에서 뺄 수 있음!!
                    if arr[ty][tx] - k < arr[y][x]:
                        arr[ty][tx] -= k
                        is_change = False
                        visit[ty][tx] = True
                        dfs(ty, tx, cnt + 1)
                        arr[ty][tx] += k
                        is_change = True
                        visit[ty][tx] = False
    else:
        ans = max(ans, cnt)


for tc in range(1, int(input()) + 1):
    N, K = map(int ,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start_point = []
    max_point = 0
    for i in arr:
        max_point = max(max_point, max(i))
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_point:
                start_point.append((i, j))
    ans = 0
    for y, x in start_point:
        visit = [[False] * N for _ in range(N)]
        visit[y][x] = True
        is_change = True
        dfs(y, x, 1)

    print('#{} {}'.format(tc, ans))