# 행렬 회전 : https://ywtechit.tistory.com/171
# 개어렵다...
# 풀이 순서 : 모래 회전해서 저장해두기 -> 토네이도 이동경로 설정 -> 모래 움직이기 구현

from collections import deque

def move_sand(x,y,idx):
    global answer
    alpha = A[x][y]
    for i in range(-2,3):
        for j in range(-2,3):
            tmp = int(A[x][y] *sand_list[idx][i+2][j+2])
            if 0<=x+i<N and 0<=y+j<N:
                A[x+i][y+j] += tmp
            else: answer+=tmp
            alpha -= tmp
    A[x][y] = 0

    #alpha 계산
    alpha_x = x+move[idx][0]
    alpha_y = y+move[idx][1]
    if 0<=alpha_x<N and 0<=alpha_y<N:
        A[alpha_x][alpha_y] += alpha
    else:
        answer+=alpha
    # for i in range(N):
        # print(*A[i])
    # print()


N = int(input())
A = [list(map(int,input().split(" "))) for _ in range(N)]
mid = N//2
q = deque([(mid, mid)])

move = [(0,-1),(1,0),(0,1),(-1,0)]
sand_list = []
sand = [[0,0,0.02,0,0],[0,0.1,0.07,0.01,0],[0.05,0,0,0,0],[0,0.1,0.07,0.01,0],[0,0,0.02,0,0]]
for _ in range(4):
    sand_list.append(sand)
    sand = list(map(list, zip(*sand)))[::-1] # 다시한번 공부할것
# print(sand_list)

cnt = 0
answer = 0
while q:
    x, y = q.popleft()
    i = cnt % 4
    for _ in range(cnt//2 +1):
        x = x + move[i][0]
        y = y + move[i][1]
        if 0<=x<N and 0<=y<N:
            move_sand(x,y,i)
            if _ == cnt//2:
                q.append((x,y))
    cnt+=1
print(answer)