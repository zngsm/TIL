N = int(input())
n_cnt = 0
n = N
while n >0:
    n_cnt += 1
    n //= 10

min_num = N - (9 * n_cnt)

for i in range(min_num, N):
    total = i
    i_copy = i
    while i_copy > 0:
        total += i_copy % 10
        i_copy //= 10
    if total == N:
        ans = i
        break
else:
    ans = 0
print(ans)