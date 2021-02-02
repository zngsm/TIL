N = int(input()) # 사람의 수
weight, tall = [], []
for _ in range(N):
    w, t = map(int, input().split())
    weight.append(w)
    tall.append(t)

# 몸무게 순회
weight_winner = []
for i in range(N):
    arr = []
    for j in range(N):
        if i == j:
            pass
        else:
            if weight[i] < weight[j]:
                arr.append(j)
    weight_winner.append(arr)

# 키 순회
tall_winner = []
for i in range(N):
    arr = []
    for j in range(N):
        if i == j:
            pass
        else:
            if tall[i] < tall[j]:
                arr.append(j)
    tall_winner.append(arr)

for i in range(N):
    new = [value for value in weight_winner[i] if value in tall_winner[i]]
    print(len(new) + 1, end=" ")
print()