# https://www.acmicpc.net/problem/1726
# 여러가지 경로중 min값을 찾아야함!
# 1트 실패 : visit을 boolean으로 해서
# 2트 실패 : 마지막 목표지점은 꼭 q에 넣어줘야함 41번줄 조건 필요
from collections import deque

def dir_command(a,b):
    if (a-1)//2 != (b-1)//2:
        return 1
    elif a != b:
        return 2
    else: return 0

def tracking(start, end):
    sx, sy, sd = start[0]-1, start[1]-1, start[2]
    ex, ey, ed = end[0]-1, end[1]-1, end[2]

    move = [(0,0), (0,1),(0,-1),(1,0),(-1,0)] #동,서,남,북
    visit = [[1000000]*N for _ in range(M)]
    visit[sx][sy] = 0

    answer = 1000000
    q = deque([(sx,sy,0,sd)]) # x,y,command수,현재방향
    while q:
        nx, ny, cnt, nd = q.popleft()
        # print(nx, ny, cnt, nd)
        if nx==ex and ny==ey:
            cnt+=dir_command(nd, ed)
            answer = min(answer, cnt)
            continue
        
        for i in range(1,5):
            for j in range(1,4):
                nnx = nx + move[i][0] * j
                nny = ny + move[i][1] * j
                if (0<=nnx<M and 0<=nny<N) and (fac[nnx][nny] == 0):
                    n_cnt = cnt+dir_command(nd,i)+1
                    if visit[nnx][nny] > n_cnt:
                        visit[nnx][nny] = n_cnt
                        q.append((nnx,nny,n_cnt,i))
                    elif nnx == ex and nny == ey:
                        q.append((nnx,nny,n_cnt,i))
                else:break
    # for i in range(M):
    #     print(*visit[i])
    return answer



M, N = map(int, input().split(" "))
fac = [list(map(int, input().split(" "))) for _ in range(M)]

start = list(map(int,input().split(" ")))
end = list(map(int,input().split(" ")))
print(tracking(start,end))