import math
N = int(input())
gosa = list(map(int,input().split(" ")))
B, C = map(int, input().split(" "))
answer = 0

for people in gosa:
    people = people-B
    answer+=1
    if people >0:
        answer+= math.ceil(people/C)
print(answer)