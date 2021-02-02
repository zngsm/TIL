import sys; sys.stdin = open("input_1247.txt", "r")

def perm(idx):
    if idx == N:
        total = 0
        for i in range(N):
            y, x = sel[i][0], sel[i][1]
            if i == 0:
                total = abs(x - startX) + abs(y - startY)
            elif i == N - 1:
                preY, preX = sel[i - 1][0], sel[i - 1][1]
                total = total + abs(x - endX) + abs(y - endY) + abs(x - preX) + abs(y - preY)
            else:
                preY, preX = sel[i - 1][0], sel[i - 1][1]
                total = total + abs(x - preX) + abs(y - preY)
        result.append(total)
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            sel.append(target[i])
            perm(idx + 1)
            visit[i] = 0
            sel.pop()


for tc in range(1, int(input()) + 1):
    N = int(input())
    input_list = list(map(int, input().split()))
    startY, startX = input_list[1], input_list[0]
    endY, endX = input_list[3], input_list[2]

    target = []
    for i in range(4, 2*(N+2), 2):
         target.append((input_list[i+1], input_list[i]))
    visit = [0] * N
    result = []
    sel = []
    perm(0)


    print('#{} {}'.format(tc, min(result)))