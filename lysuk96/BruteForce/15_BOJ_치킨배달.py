# https://www.acmicpc.net/problem/15686
from itertools import combinations
from math import inf

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


N, M = map(int, input().split( ))
village = [list(map(int, input().split( ))) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            home.append((i,j))
        elif village[i][j] == 2:
            chicken.append((i,j))

answer = inf
for comb in combinations([i for i in range(len(chicken))], M):
    tmp = 0
    for h in home:
        local_min = inf
        for idx in comb:
            local_min = min(local_min, dist(h, chicken[idx]))
        tmp += local_min
    answer = min(answer, tmp)
print(answer)