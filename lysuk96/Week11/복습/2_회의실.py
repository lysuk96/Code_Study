N = int(input())
timetable = [tuple(map(int,input().split(" "))) for _ in range(N)]
timetable.sort(key=lambda x:(x[0],x[1]))

answer=0
next = 0
for start, end in timetable:
    if end < next:
        next = end
    elif next <= start:
        answer+=1
        next = end
        # print(now, next)

# print(timetable)
# for start, end in timetable:
#     if now <= start:
#         now = end
#         # print(now)
#         answer+=1
print(answer)
