from itertools import combinations
from math import inf
N = int(input())
stat = [list(map(int,input().split())) for _ in range(N)]

all = [i for i in range(N)]
answer = inf
for start in combinations(all, N//2):
    link = list(set(all) - set(start))
    start_sum = 0
    link_sum = 0
    for a,b in combinations(start, 2):
        start_sum += stat[a][b] + stat[b][a]
    for a,b in combinations(link, 2):
        link_sum += stat[a][b] + stat[b][a]
    answer = min(answer, abs(start_sum - link_sum))
    
print(answer)
    