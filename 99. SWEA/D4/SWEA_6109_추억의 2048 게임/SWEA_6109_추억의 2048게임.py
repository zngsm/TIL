import sys; sys.stdin = open("input_6109.txt", "r")

def search(r, c):
    if arr[r][c] == 0:
        return
    ty = r + dy[dir]
    tx = c + dx[dir]
    if ty < 0 or ty >= N or tx < 0 or tx >= N:
        return
    if arr[ty][tx] == arr[r][c]:
        arr[ty][tx] = str(arr[r][c] * 2)
        arr[r][c] = 0
        return
    if arr[ty][tx] == 0:
        y, x = r, c
        while True:
            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                break
            if arr[ty][tx] == arr[y][x]:
                arr[ty][tx] = str(arr[y][x] * 2)
                arr[y][x] = 0
                break
            if arr[ty][tx] != 0 and arr[y][x] != arr[ty][tx]:
                break
            arr[ty][tx] = arr[y][x]
            arr[y][x] = 0
            y, x = ty, tx
            ty += dy[dir]
            tx += dx[dir]
    return

for tc in range(1, int(input()) + 1):
    N, d = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    direction = ['up', 'down', 'left', 'right']

    dir = direction.index(d)
    if dir == 0 or dir == 2:
        for i in range(N):
            for j in range(N):
              search(i,j)
    else:
        for i in range(N-1, -1,-1):
            for j in range(N-1, -1, -1):
                search(i, j)

    print('#{}'.format(tc))
    for ans in arr:
        print(*ans)