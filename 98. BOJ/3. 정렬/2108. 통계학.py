import sys

s = sys.stdin.readline

N = int(s())
arr = list(int(s()) for _ in range(N))
ans = arr.sort()
cnt = {}
for i in ans:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
min = 4001
c = 0
for k, v in cnt.items():
    if v == max(cnt.values()):
        if c >= 2:
            break
        else:
            min = k
            c += 1
ans1 = round(sum(ans) / N)
ans2 = ans[N//2]
ans3 = min
ans4 = ans[-1] - ans[0]

print(ans1, ans2, ans3, ans4, sep='\n')