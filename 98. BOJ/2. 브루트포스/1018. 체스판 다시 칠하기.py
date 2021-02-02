def black_start(y, x):
    global min_cnt
    cnt = 0
    is_break = False
    # 해당 점을 기준으로 짝수행일때 -> 짝수열은 같은 색 / 홀수열은 다른 색 / 홀수행일 때 -> 짝수열은 다른 색 / 홀수열은 같은 색
    for i in range(y, y + 8):
        if i % 2: # 홀 수 일때
            for j in range(x, x + 8):
                if j % 2: # 홀 수 일때
                    if arr[i][j] != 'B':
                        cnt += 1
                else:
                    if arr[i][j] == 'B':
                        cnt += 1

                if cnt >= min_cnt:
                    is_break = True
                    break
        else: # 짝 수 일때
            for j in range(x, x + 8):
                if j % 2: # 홀 수 일때
                    if arr[i][j] == 'B':
                        cnt += 1
                else:
                    if arr[i][j] != 'B':
                        cnt += 1
                if cnt >= min_cnt:
                    is_break = True
                    break
        if is_break:
            return
    else:
        min_cnt = min(min_cnt, cnt)

def white_start(y, x):
    global min_cnt
    cnt = 0
    is_break = False
    # 해당 점을 기준으로 짝수행일때 -> 짝수열은 같은 색 / 홀수열은 다른 색 / 홀수행일 때 -> 짝수열은 다른 색 / 홀수열은 같은 색
    for i in range(y, y + 8):
        if i % 2: # 홀 수 일때
            for j in range(x, x + 8):
                if j % 2: # 홀 수 일때
                    if arr[i][j] != 'W':
                        cnt += 1
                else:
                    if arr[i][j] == 'W':
                        cnt += 1

                if cnt >= min_cnt:
                    is_break = True
                    break
        else: # 짝 수 일때
            for j in range(x, x + 8):
                if j % 2: # 홀 수 일때
                    if arr[i][j] == 'W':
                        cnt += 1
                else:
                    if arr[i][j] != 'W':
                        cnt += 1
                if cnt >= min_cnt:
                    is_break = True
                    break
        if is_break:
            return
    else:
        min_cnt = min(min_cnt, cnt)

N, M = map(int, input().split()) # 세로, 가로
arr = [list(input()) for _ in range(N)]

min_cnt = 65
for i in range(0, N - 7):
    for j in range(0, M - 7):
        black_start(i, j)
        white_start(i, j)
print(min_cnt)