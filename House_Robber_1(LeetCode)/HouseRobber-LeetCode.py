def maxSumTopDown(arr):
    """
    TC - O(n)
    SC - O(n) + O(n)
    """
    def getSum(idx, dp):
        if idx == 0:
            return arr[idx]
        
        if idx < 0:
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        pick = arr[idx] + getSum(idx - 2, dp)
        notPick = 0 + arr[idx - 1]

        dp[idx] = max(pick, notPick)
        return dp[idx]
    
    dp = [-1 for _ in range(len(arr) + 1)]
    return getSum(len(arr) - 1, dp)

def maxSumBottomUp(arr):
    """
    TC - O(n)
    SC - O(n)
    """
    def getSum(dp):
        dp[0] = arr[0]
        negative = 0

        for i in range(1, len(arr)):
            pick = arr[i]
            if i > 1:
                pick += dp[i - 2]
            notPick = 0 + dp[i - 1]
            
            dp[i] = max(pick, notPick)
        
        return dp[len(arr) - 1]
    
    dp = [-1 for _ in range(len(arr) + 1)]
    return getSum(dp)

def maxSumBottomUpOptimized(arr):
    """
    TC - O(n)
    SC - O(1)
    """
    prev = arr[0]
    prevOfPrev = 0
    for i in range(1, len(arr)):
        take = arr[i]
        if i > 1:
            take += prevOfPrev
        notTake = 0 + prev
        curr = max(take, notTake)
        prevOfPrev = prev
        prev = curr
    return prev


if __name__ == '__main__':
    arr = [3, 1, 5, 9]
    # result = maxSumTopDown(arr)
    # result = maxSumBottomUp(arr)
    result = maxSumBottomUpOptimized(arr)
    print(result)