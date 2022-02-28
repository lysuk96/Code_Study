# https://www.acmicpc.net/problem/2493
# 문제 예술인듯.. 스택 정리할때 한번 더 풀어볼 것!
from collections import deque

N = int(input())
tops= list(map(int, input().split(" ")))
q = deque([(t,i) for i,t in enumerate(tops)])
s = deque([])
answer = [0]*N

s.append(q.popleft())
# print(s, q)

while q:
    top, idx = q.popleft()
    tmp = []
    # print(s)
    while s:
        s_top, s_idx = s[-1]
        if s_top > top:
            answer[idx] = s_idx+1
            break
        else:
            s.pop()
    # tmp.reverse() #이거해주면 O(N)이 될수가 없삼
    # s.extend(tmp)
    s.append((top, idx))

print(*answer)
