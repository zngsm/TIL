import sys; sys.stdin = open("input_1873.txt", "r")

# 상하좌우 델타
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direction = ['^', 'v', '<', '>']
control_dir = ['U', 'D', 'L', 'R']

# 상화좌우 조작 함수
def control(y, x, d):
    arr[y][x] = direction[d]
    targety, targetx = y + dy[d], x + dx[d]
    if 0 <= targety < H and 0 <= targetx < W and arr[targety][targetx] == '.':
        arr[targety][targetx] = direction[d]
        arr[y][x] = '.'
        return targety, targetx, d
    return y, x, d

# 포탄 발사시 함수
def shoot(y, x, d):
    y, x = y + dy[d], x + dx[d]
    while 0 <= y < H and 0 <= x < W:
        if arr[y][x] == '*':
            arr[y][x] = '.'
            break
        if arr[y][x] == '#':
            break
        y, x = y + dy[d], x + dx[d]


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split()) # 높이 H, 넓이 W
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    control_key = list(input())

    # 시작 y, x 좌표와 방향 설정하기
    for i in range(H):
        for j in range(W):
            if arr[i][j] in direction:
                starty, startx, dir = i, j, direction.index(arr[i][j])

    for i in range(N):
        if control_key[i] == 'S':
            shoot(starty, startx, dir)
        else:
            starty, startx, dir = control(starty, startx, control_dir.index(control_key[i]))


    print('#{}'.format(tc), end=" ")
    for i in range(H):
        for j in range(W):
            print(arr[i][j], end="")
        print()


