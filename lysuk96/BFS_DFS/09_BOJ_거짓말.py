# https://www.acmicpc.net/problem/1043
from collections import defaultdict, deque
from itertools import combinations

N, M = map(int, input().split(" "))
visit = [False]*(N+1)

q = deque(list(map(int, input().split(" "))))
q.popleft()
# for t in truth:
#     visit[t] = True

tree = defaultdict(set)
party_set = []
for _ in range(M):
    party = list(map(int, input().split(" ")))
    party.pop(0)
    party_set.append(party)
    for x, y in combinations(party, 2):
        tree[x].add(y)
        tree[y].add(x)

while q:
    tmp = q.popleft()
    visit[tmp] = True
    for t in tree[tmp]:
        if not visit[t]:
            q.append(t)

# print(tree)
# print(visit)

answer=0
for party in party_set:
    flag = True
    for p in party:
        if visit[p]:
            flag = False
            break
    if flag:
        answer+=1
print(answer)
# for i in range(N):
#     if visit[i]:


