import sys; sys.stdin = open("input_13305.txt", "r")
s = sys.stdin.readline

N = int(s())
road = list(map(int, s().split()))
station = list(map(int, s().split()))

pick = station[0]
cost = 0
dist = 0
for i in range(1, N):
    dist += road[i - 1]
    if station[i] < pick:
        cost += (dist * pick)
        pick = station[i]
        dist = 0
else:
    cost += (dist * pick)
print(cost)