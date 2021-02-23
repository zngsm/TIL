N = int(input())
cnt = 0
ans = 666
while cnt < N:
    ans_str = str(ans)
    if '666' in ans_str:
        cnt += 1
        result = ans
    ans += 1
print(result)