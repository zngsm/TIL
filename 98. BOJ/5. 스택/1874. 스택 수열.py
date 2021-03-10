import sys; sys.stdin = open("input_1874.txt", "r")
s = sys.stdin.readline
cnt = 0
result = []
stack = []
is_False = False
N = int(s())
for _ in range(N):
    num = int(s())

    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

for r in result:
    print(r)
