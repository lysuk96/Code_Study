from collections import defaultdict
def is_able(x,y,c):
    for i in range(c):
        for j in range(c):
            if 0<=x+i<10 and 0<=y+j<10:
                if paper[x+i][y+j] != 1:
                    return False
            else:
                return False
    return True

def put_on(x,y,c):
    for i in range(c):
        for j in range(c):
            if 0<=x+i<10 and 0<=y+j<10:
                paper[x+i][y+j] = c+1


colors = [5,4,3,2,1]
dic = defaultdict(int)
for c in colors:
    dic[c]=5

paper = [list(map(int,input().split(" "))) for _ in range (10)]
answer = 0
for k in colors:
    for i in range(10):
        for j in range(10):
            if is_able(i,j,k) and dic[k]>0:
                put_on(i,j,k)
                answer+=1
                dic[k]-=1


flag = True
print()
for i in range(10):
    print(*paper[i])
    if 1 in paper[i]:
        flag = False
        break
if flag:
    print(answer)
else:print(-1)