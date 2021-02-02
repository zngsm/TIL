n = int(input())

cnt = 0
t = n
while cnt == 0 or t != n:
    if t > 9: # 두자리수일 경우
        t = (t % 10) * 10 + (((t // 10) + (t % 10)) % 10)
    else:
        t = t * 10 + t

    cnt += 1

print(cnt)