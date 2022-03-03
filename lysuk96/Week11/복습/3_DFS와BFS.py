from collections import defaultdict,deque

def dfs(x):
    print(x, end = ' ')
    for node in v[x]:
        if not visit_d[node]:
            visit_d[node]= True
            dfs(node)
    return

def bfs():
    q = deque({V})
    visit_b = [False]*(N+1)
    visit_b[V] = True
    while q:
        tmp = q.popleft()
        print(tmp, end = ' ')
        for node in v[tmp]:
            if not visit_b[node]:
                visit_b[node]=True
                q.append(node)


N, M, V = map(int, input().split(" "))
v = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split(" "))
    v[s].append(e)
    v[e].append(s)

for key in v:
    v[key].sort()

# dfs
visit_d = [False]*(N+1)
visit_d[V] = True
dfs(V)
print()

#bfs
bfs()



