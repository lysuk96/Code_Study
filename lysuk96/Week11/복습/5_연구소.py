from itertools import combinations
from copy import deepcopy
from collections import deque

def bfs_n_cnt(map):
    q = deque(virus)
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            


N, M = map(int, input().split(" "))
yeongu = [list(map(int,input().split(" "))) for _ in range(N)]

virus = []
air = []
for i in range(N):
    for j in range(M):
        if yeongu[i][j] == 2:
            virus.append((i,j))
        elif yeongu[i][j] == 0:
            air.append((i,j))

for comb in combinations(air, 3):
    new_map = deepcopy(yeongu)
    for x,y in comb:
        new_map[x][y] = 1
    bfs_n_cnt(new_map)

