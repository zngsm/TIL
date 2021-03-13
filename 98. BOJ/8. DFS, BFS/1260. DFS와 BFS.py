import sys; sys.stdin = open("input_1260.txt", "r")
s = sys.stdin.readline

def dfs(i):
    dfs_visit.append(i)
    for w in sorted(arr[i]):
        if w not in dfs_visit:
            dfs(w)
    return dfs_visit


def bfs(i):
    Q = [i]
    bfs_visit.append(i)
    while Q:
        v = Q.pop(0)
        for w in sorted(arr[v]):
            if w not in bfs_visit:
                Q.append(w)
                bfs_visit.append(w)
    return bfs_visit

N, M, V = map(int, s().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    st, ed = map(int, s().split())
    arr[st].append(ed)
    arr[ed].append(st)

dfs_visit, bfs_visit = [], []
dfs_ans = dfs(V)
bfs_ans = bfs(V)
print(*dfs_ans)
print(*bfs_ans)