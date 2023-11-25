def climbStairs(n):

    def jump(n, dp):
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    dp = [-1 for _ in range(n + 1)]
    result = jump(n, dp)
    return result

if __name__ == '__main__':
    result = climbStairs(4)
    print(result)