days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
flowers = []
for i in range(1, 13):
    days[i]+=days[i-1]

N = int(input())
for _ in range(N):
    s_m, s_d, e_m, e_d= map(int, input().split(" "))
    s_day = days[s_m-1]+s_d
    e_day = days[e_m-1]+e_d
    flowers.append((s_day, e_day))
flowers.sort(key = lambda x:x[0])
# print(flowers)

now = days[2]+1
next = 0
answer = 0

for start, end in flowers:
    if next>days[11]:
        break
    if start<= now < end:
        if next<end:
            next = end
    else:
        if start<= next < end:
            answer+=1
            now = next
            next= end
        elif end <=next:
            continue
        else:
            break

if next <= days[11]:
    print(0)
else:
    print(answer+1)




