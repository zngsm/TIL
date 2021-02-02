def solve(y, x):
    visit = [[0] * N for _ in range(N)]
    visit[y][x] = 1
    for i in range(N):
        visit[y][i] = 1
        visit[i][x] = 1



N = int(input())

for i in range(N):
    for j in range(N):
        visit = [[0] * N for _ in range(N)]
        visit[i][j] = 1

