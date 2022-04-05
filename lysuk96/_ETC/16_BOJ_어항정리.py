# https://www.acmicpc.net/problem/23291
def levitate_half():
    global pool
    pool = [pool[-1][:N//2][::-1],pool[-1][N//2:]]
    # print(pool)

    tmp = [pool[0][:N//4],pool[1][:N//4]]
    tmp = rotate(rotate(tmp))
    # print(tmp)

    pool = [pool[0][N//4:], pool[1][N//4:]]
    for i in range(2):
        pool.insert(0,tmp[i][::-1])
    # print(pool)

    fish_exchange()

def fish_exchange():
    global pool
    a = len(pool)
    b = len(pool[0])
    c = len(pool[-1])-b
    tmp1 = [[0]*b for _ in range(a)] #직사각형
    tmp2 = [0]*(c+b) #남은 일렬

    # 직사각형 차이 구하기
    for i in range(a):
        for j in range(b):
            if i+1<a:
                d = abs(pool[i+1][j] - pool[i][j]) //5
                if d>0:
                    if pool[i+1][j] > pool[i][j]:
                        tmp1[i+1][j] -=d
                        tmp1[i][j] +=d
                    else:
                        tmp1[i][j] -=d
                        tmp1[i+1][j] +=d
            if j+1<b:
                d = abs(pool[i][j] - pool[i][j+1]) //5
                if d>0:
                    if pool[i][j+1]>pool[i][j]:
                        tmp1[i][j+1]-=d
                        tmp1[i][j]+=d
                    else:
                        tmp1[i][j+1]+=d
                        tmp1[i][j]-=d
    # print(tmp1)
    
    # 일렬 차이 구하기
    for j in range(b-1, b+c):
        if j+1<b+c:
            d = abs(pool[-1][j+1]- pool[-1][j]) // 5
            if d>0:
                if pool[-1][j+1]>pool[-1][j]:
                    tmp2[j+1]-=d
                    tmp2[j]+=d
                else:
                    tmp2[j+1]+=d
                    tmp2[j]-=d
    # print(tmp2)

    for i in range(a):
        for j in range(b):
            pool[i][j]+=tmp1[i][j]
    for j in range(b-1,b+c):
        pool[-1][j]+=tmp2[j]
    # print(pool)

    # 다시 일렬만들기
    tmp3 = []
    for j in range(b):
        for i in range(a-1,-1,-1):
            tmp3.append(pool[i][j])
    for j in range(b, b+c):
        tmp3.append(pool[-1][j])
    pool=[tmp3]
    # print(pool)

def rotate(arr):
    return list(map(list, zip(*arr[::-1])))[::-1]

def levitate():
    global pool
    pool.insert(0,[pool[0].pop(0)])
    # print(pool)
    while True:
        a = len(pool)
        b = len(pool[0])
        c = len(pool[-1])-b
        if c < a: break

        tmp = [*pool[:-1], pool[-1][:b]]
        pool = [pool[-1][b:]]
        # print(tmp)
        tmp = rotate(tmp)
        # print(tmp)

        for tmp_pool in tmp:
            pool.insert(0, tmp_pool)
    # print(pool)

N, K = map(int, input().split( ))
global pool
pool = [list(map(int,input().split( )))]

dif = max(pool[0]) - min(pool[0])
answer = 0
while dif > K:
    answer+=1

    #1. min에 1넣기
    fish_min = min(pool[0])
    for i in range(N):
        if pool[0][i] == fish_min:
            pool[0][i]+=1
    
    #2. 공중부양
    levitate()

    #3. 어항 물고기 조절하고 일렬만들기
    fish_exchange()

    #4. 절반 공중부양
    levitate_half()

    dif = max(pool[0]) - min(pool[0])


print(answer)