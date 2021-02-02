import sys; sys.stdin = open("input_4615.txt", "r")


dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def solve(Y, X, color):
    arr[Y][X] = color
    change = []
    for i in range(8):
        ty = Y + dy[i]
        tx = X + dx[i]
        while True:
            if ty < 0 or ty > N or tx < 0 or tx > N or arr[ty][tx] == 0:
                change = []
                break
            if arr[ty][tx] == color:
                break
            else:
                change.append((ty, tx))
            ty = ty + dy[i]
            tx = tx + dx[i]
        color_change(change)

def color_change(array):
    for Y, X in array:
        if color == 1:
            arr[Y][X] = 1
        else:
            arr[Y][X] = 2

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[N//2][N//2] = arr[(N//2)+1][(N//2)+1] = 2
    arr[(N//2)+1][N//2] = arr[N//2][(N//2)+1] = 1
    for i in range(M):
        y, x, color = map(int, input().split())
        solve(y, x, color)

    black = white = 0
    for i in range(N + 1):
        black += arr[i].count(1)
        white += arr[i].count(2)
    print('#{} {} {}'.format(tc, black, white))