# https://www.acmicpc.net/problem/16234
from collections import deque

def print_cont():
    print()
    for i in range(N):
        print(*cont[i])

def bfs(a,b):
    target = [(a,b)]
    q = deque([(a,b)])
    visit[a][b] = True
    person = cont[a][b]
    cnt = 1
    while q:
        _x, _y = q.popleft()
        for i in range(4):
            _nx = _x + move[i][0]
            _ny = _y + move[i][1]
            if 0<=_nx<N and 0<=_ny<N:
                if not visit[_nx][_ny] and is_open(cont[_nx][_ny], cont[_x][_y]):
                    visit[_nx][_ny] = True
                    q.append((_nx,_ny))
                    cnt += 1
                    person += cont[_nx][_ny]
                    target.append((_nx,_ny))
    
    return target, person // cnt

def is_open(a,b):
    return L<=abs(b-a)<=R

N, L, R = map(int, input().split())
cont = [list(map(int, input().split())) for _ in range(N)]
move = [(0,1),(1,0),(-1,0),(0,-1)]

answer = 0
while True:
    flag = True

    candidate= []
    people = []
    visit = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for k in range(2):
                if visit[x][y]: continue
                nx = x + move[k][0]
                ny = y + move[k][1]
                if 0<=nx<N and 0<=ny<N and is_open(cont[x][y], cont[nx][ny]):
                    target, new_person = bfs(x,y)
                    candidate.append(target)
                    people.append(new_person)
                    flag = False

    for idx, cand in enumerate(candidate):
        for i, j in cand:
            cont[i][j] = people[idx]

    if flag:
        break
    answer+=1
    # print_cont()
    
print(answer)