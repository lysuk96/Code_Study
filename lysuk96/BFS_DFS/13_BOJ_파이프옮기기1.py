# https://www.acmicpc.net/problem/17070
# 어째서 재귀로 푼 dfs 가 더 빠른가...
import sys

input = sys.stdin.readline
N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))
total = 0


def dfs(x, y, direction):
    global total
    if x == N - 1 and y == N - 1 and house[x][y] == 0:
        total += 1
        return
    if direction == 0 or direction == 2:
        if y  < N - 1:
            if house[x][y + 1] == 0:
                dfs(x, y + 1, 0)
    if direction == 1 or direction == 2:
        if x < N - 1:
            if house[x + 1][y] == 0:
                dfs(x + 1, y, 1)
    if direction == 0 or direction == 1 or direction == 2:
        if x < N - 1 and y < N - 1:
            if house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)
print(total)

# from collections import deque

# def can_move(x,y,d):
#     if d==0:
#         if 0<=y+1<N and home[x][y+1]==0:
#             return True
#         return False
#     elif d==1:
#         tmp = [(0,1),(1,0),(1,1)]
#         for dx, dy in tmp:
#             nx = x +dx
#             ny = y + dy
#             if 0<=nx<N and 0<=ny<N and home[nx][ny] == 0:
#                 continue
#             else:
#                 return False
#         return True
#     elif d == 2:
#         if 0<=x+1<N and home[x+1][y]==0:
#             return True
#         return False


# N = int(input())
# home = [list(map(int,input().split(" "))) for _ in range(N)]

# m = [(0,1),(1,1),(1,0)] #위, 위대, 오, 아대, 아
# move = [(m[0],m[1],(-1,-1)),(m[0],m[1],m[2]),((-1,-1),m[1],m[2])]

# q = deque([(0,1,0)])
# answer = 0
# while q:
#     x, y, d = q.popleft()
#     if x == y == N-1:
#         answer+=1
#     for i, (dx, dy) in enumerate(move[d]):
#         if dx == dy == -1:
#             continue
#         nx = x + dx
#         ny = y + dy
#         if can_move(x,y,i):
#             q.append((nx,ny,i))

# print(answer)


