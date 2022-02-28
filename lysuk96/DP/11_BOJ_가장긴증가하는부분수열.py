N = int(input())
nums = list(map(int, input().split(" ")))
dp = [0]*N

for i in range(N):
    target_idx = -1
    for j in range(0, i):
        if nums[j]<nums[i] and dp[j]>dp[target_idx]:
            target_idx = j
    if target_idx ==-1:
        dp[i] = 1
    else:
        dp[i] = max(dp[target_idx]+1, dp[i])
print(max(dp))
