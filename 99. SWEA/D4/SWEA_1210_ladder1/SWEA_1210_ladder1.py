import sys; sys.stdin = open("input_1210.txt", "r")

dy = [0, 0, -1] # 좌 우 상
dx = [-1, 1, 0]

def search(y, x):
    global ans
    if y == 0:
        return x
    visit[y][x] = 1
    for i in range(3):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx >= 100 or ty >= 100 or tx < 0 or arr[ty][tx] == 0:
            continue
        if visit[ty][tx]:
            continue
        return search(ty, tx)
        # visit[ty][tx] = 0

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    is_break = False
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                endY = i
                endX = j
                is_break = True
                break
        if is_break:
            break
    visit = [[0] * 100 for _ in range(100)]
    ans = search(endY, endX)
    print('#{} {}'.format(tc, ans))