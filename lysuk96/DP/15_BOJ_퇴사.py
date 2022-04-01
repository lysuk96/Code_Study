N = int(input())
sched = [tuple(map(int, input().split( ))) for _ in range(N)]
dp = [0] *(N+1)
for i in range(N-1, -1, -1):
    ti, pi = sched[i]
    if i + ti <= N:
        dp[i] = max(dp[i+ti]+pi, dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])