def search(cnt, total):
    global max_num
    if total > M:
        return
    if cnt == 3:
        max_num = max(max_num, total)
        return

    for i in range(N):
        if visit[i]:
            continue
        visit[i] = 1
        new_total = total + card[i]
        search(cnt + 1, new_total)
        visit[i] = 0
        new_total -= card[i]



N, M = map(int, input().split())
card = list(map(int, input().split()))
visit = [0] * N
max_num = 0
search(0, 0)
print(max_num)
# N장의 카드, 3개를 뽑아서 M을 넘지 않으며, M과 최대한 가까운 카드

