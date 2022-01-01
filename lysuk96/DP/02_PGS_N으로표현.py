#N으로 표현(실패)
#DP를 숫자 기준으로 만들지 말고, N이 몇번 쓰였는지로 계산해라!

def solution(N, number):
    dp = [[]]
    for i in range(1,9):
        tmp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i -j]:
                    tmp.append(k+l)
                    tmp.append(k*l)
                    if l != 0:
                        tmp.append(k//l)
                    if k - l>0:
                        tmp.append(k-l)
        tmp.append(int(str(N)*i))
        dp.append(list(set(tmp)))
        if number in dp[i]:
            return i

    return -1

print(solution(2,11))
