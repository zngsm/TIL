def search(cnt, total):
    global ans
    if ans:
        return
    if total > 100:
        return
    if cnt == 7:
        if total == 100:
            for i in range(9):
                if visit[i]:
                    ans.append(dwarves[i])
            return
        return

    for i in range(9):
        if visit[i] and not ans:
            continue
        visit[i] = 1
        new_total = total + dwarves[i]
        search(cnt + 1, new_total)
        visit[i] = 0
        new_total -= dwarves[i]


dwarves = [int(input()) for _ in range(9)]
visit = [0] * 9
ans = []
search(0, 0)
for i in sorted((ans)):
    print(i)