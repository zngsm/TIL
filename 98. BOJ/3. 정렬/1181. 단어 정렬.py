import sys; sys.stdin = open("input_1181.txt", "r")
s = sys.stdin.readline
N = int(s())
arr = [s().replace("\n", "", 1) for _ in range(N)]
ans = sorted(arr)
ans = sorted(ans, key= lambda x: len(x))
result = []
for i in ans:
    if i not in result:
        result.append(i)
        print(i)