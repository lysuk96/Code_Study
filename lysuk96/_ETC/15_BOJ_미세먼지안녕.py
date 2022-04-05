# https://www.acmicpc.net/problem/17144
# 1. 어떻게 동시성을 줄 것인가?
# 2. 공기청정기에서 바람 나오는 것 구현할때 오래걸림 -> deepcopy말고 다른방법..?
from copy import deepcopy


def spread(x,y):
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = 0
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0<=nx<R and 0<=ny<C and room[nx][ny]!=-1:
            cnt+=1
            tmp[nx][ny] += room[x][y] // 5
    tmp[x][y] += room[x][y] - (room[x][y] // 5) * cnt
    # print(tmp)
    

def spread_dust():
    global room
    for i in range(R):
        for j in range(C):
            if room[i][j]!=0 and room[i][j]!=-1:
                spread(i,j)
    room = tmp

def get_dust_cleaner():
    for i in range(R):
        if room[i][0] == -1: return i

def blow(sx, move):
    global room
    room_tmp = deepcopy(room)
    x = sx
    y = 0
    i=0
    room[x][y] = 0
    while True:
        if not(0<=x + move[i][0]<R and 0<=y + move[i][1]<C):
            i+=1

        nx = x + move[i][0]
        ny = y + move[i][1]
        if nx == sx and ny ==0:
            break

        room_tmp[nx][ny] = room[x][y]

        x = nx
        y = ny
    room = room_tmp

def wind_blow(x):
    blow(x, [(0,1),(-1,0),(0,-1),(1,0)]) #upper blow
    blow(x+1, [(0,1),(1,0),(0,-1),(-1,0)]) #lower blow

def print_room():
    print()
    for r in room:
        print(*r)

R, C, T= map(int, input().split( ))
global room
room = [list(map(int, input().split( ))) for _ in range(R)]
cx = get_dust_cleaner()

for time in range(T):
    tmp = [[0]*C for _ in range(R)]
    tmp[cx][0], tmp[cx+1][0] = -1, -1
    # print(tmp)
    spread_dust()

    # print_room()
    wind_blow(cx)
# print_room()

answer= 0
for r in room:
    answer += sum(r)
print(answer+2)