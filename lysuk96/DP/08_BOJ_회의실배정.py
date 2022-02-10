#https://www.acmicpc.net/problem/1931
N = int(input())
candidate = []
for i in range(N):
    start, end = input().split(" ")
    candidate.append((int(start), int(end)))

candidate.sort(key = lambda x: x[0])
candidate.sort(key = lambda x: x[1])

answer = []
left = 0
for start, end in candidate:
    if left <= start:
        left = end
        answer.append((start,end))
# print(candidate)
print(len(answer))