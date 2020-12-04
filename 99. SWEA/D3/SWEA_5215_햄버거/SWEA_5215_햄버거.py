import sys; sys.stdin = open("input_5215.txt", "r")

def powerset(idx, kcal, score):
    if kcal > L:
        return

    if idx == N:
        if not result:
            result.append(score)
        else:
            if max(result) < score:
                result.append(score)
        return

    sel[idx] = 1
    total_kcal = kcal + hamburger[idx][1]
    total_score = score + hamburger[idx][0]
    powerset(idx + 1, total_kcal, total_score)

    sel[idx] = 0
    total_kcal = total_kcal - hamburger[idx][1]
    total_score = total_score - hamburger[idx][0]
    powerset(idx + 1, total_kcal, total_score)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    hamburger = [list(map(int, input().split())) for _ in range(N)]
    sel = [0] * N
    result = []
    powerset(0, 0, 0)
    print('#{} {}'.format(tc, max(result)))