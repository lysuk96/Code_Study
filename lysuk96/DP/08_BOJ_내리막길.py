# from collections import deque
import sys
sys.setrecursionlimit(100000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if mp[nx][ny] < mp[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n = map(int, input().split(" "))
mp = [list(map(int, input().split(" "))) for _ in range (m)]
dp = [[-1]*n for _ in range(m)]

print(dfs(0,0))
# print(mp)
# print(dp)
