import sys; sys.stdin = open("input_1953.txt", "r")

search = {
    1 : [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2 : [(-1, 0), (1, 0)],
    3 : [(0, -1), (0, 1)],
    4 : [(-1, 0), (0, 1)],
    5 : [(1, 0), (0, 1)],
    6 : [(1, 0), (0, -1)],
    7 : [(-1, 0), (0, -1)]
}


for tc in range(1, int(input()) + 1):
    N, M, y, x, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = [[0] * M for _ in range(N)]
    queue = []
    queue.append((y, x))
    visit[y][x] = 1
    while queue:
        r, c = queue.pop(0)
        if visit[r][c] == T:
            break
        idx = arr[r][c]
        for i in range(len(search[idx])):
            ty = r + search[idx][i][0]
            tx = c + search[idx][i][1]
            if 0 <= ty < N and 0 <= tx < M and visit[ty][tx] == 0:
                if search[idx][i] == (-1, 0):
                    if arr[ty][tx] == 1 or arr[ty][tx] == 2 or arr[ty][tx] == 5 or arr[ty][tx] == 6:
                        queue.append((ty, tx))
                        visit[ty][tx] = visit[r][c] + 1
                elif search[idx][i] == (1, 0):
                    if arr[ty][tx] == 1 or arr[ty][tx] == 2 or arr[ty][tx] == 4 or arr[ty][tx] == 7:
                        queue.append((ty, tx))
                        visit[ty][tx] = visit[r][c] + 1
                elif search[idx][i] == (0, -1):
                    if arr[ty][tx] == 1 or arr[ty][tx] == 3 or arr[ty][tx] == 4 or arr[ty][tx] == 5:
                        queue.append((ty, tx))
                        visit[ty][tx] = visit[r][c] + 1
                else:
                    if arr[ty][tx] == 1 or arr[ty][tx] == 3 or arr[ty][tx] == 6 or arr[ty][tx] == 7:
                        queue.append((ty, tx))
                        visit[ty][tx] = visit[r][c] + 1

    cnt = 0
    for i in visit:
        for j in i:
            if 0 < j <= T:
                cnt += 1
    print('#{} {}'.format(tc, cnt))