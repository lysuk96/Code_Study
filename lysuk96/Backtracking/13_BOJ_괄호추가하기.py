# https://www.acmicpc.net/problem/16637
# https://dirmathfl.tistory.com/276
# eval 함수 : str으로 있는 식을 계산해서 return
# 다시 풀 것 추천

from math import inf
def tracking(idx, sub_sik):
    global answer
    if idx == len(op):
        answer = max(answer, int(sub_sik))
        return
    
    # (3+8) *7-9*2
    first = str(eval(sub_sik + op[idx] + nums[idx]))
    tracking(idx+1, first)

    # 3+ (8*7) -9*2
    if idx+1<len(op):
        second = str(eval(sub_sik + op[idx] + '(' +\
            nums[idx] + op[idx+1]+ nums[idx+1]+')'))
        tracking(idx+2, second)



N = int(input())
sik = input()
nums, op = [], []
for s in sik:
    nums.append(s) if s.isdigit() else op.append(s)

answer = -inf
tracking(0,nums.pop(0))
print(answer)