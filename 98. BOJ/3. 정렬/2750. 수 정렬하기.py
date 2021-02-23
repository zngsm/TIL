N = int(input())
result = []

for _ in range(N):
    a = int(input())
    if not result:
        result.append(a)
    else:
        for i in range(len(result)):
            if a < result[i]:
                result.insert(i, a)
                break
        else:
            result.append(a)
for r in result:
    print(r)