# https://www.acmicpc.net/problem/17135
# 1트 실패 : 거리 관련 문제 조건을 똑바로 안읽어서 틀림

from copy import deepcopy
from itertools import combinations
from math import inf

def attack(y):
    for i in range(0, D):
        for j in range(-i, i+1):
            nx = N -(i+1-abs(j))
            ny = y+j
            if 0<=nx<N and 0<=ny<M and castle[nx][ny] == 1:
                return (nx, ny)
    return None

def remove(target):
    global tmp
    for x,y in target:
        castle[x][y] = 0
        tmp+=1

N, M, D = map(int, input().split(" "))
_map = [list(map(int,input().split(" "))) for _ in range(N)]
c = [i for i in range(M)]
answer = -inf
for hunters in combinations(c, 3):
    castle = deepcopy(_map)
    tmp = 0
    for _ in range(N):
        target = set()
        for h in hunters:
            enemy = attack(h)
            if enemy is not None : target.add(enemy)
        if target : 
            remove(target)
        castle.insert(0, [0]*M)
        castle.pop(-1)
    answer = max(answer, tmp)
print(answer)