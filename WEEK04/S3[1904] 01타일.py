n = int(input())

def tile(n):
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    if n == 1:
        return dp[1]
    if n == 2:
        return dp[2]

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
    return dp[n]

print(tile(n))