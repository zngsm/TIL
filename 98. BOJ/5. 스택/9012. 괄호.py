import sys; sys.stdin = open("input_9012.txt", "r")
s = sys.stdin.readline

N = int(s())
for _ in range(N):
    arr = list(s())
    total = 0
    for i in arr:
        if i == '(':
            total += 1
        elif i == ')':
            if total > 0:
                total -= 1
            else:
                ans = 'NO'
                break
    else:
        if total != 0:
            ans = 'NO'
        else:
            ans = 'YES'

    print(ans)