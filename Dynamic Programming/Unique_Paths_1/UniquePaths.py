"""
We have to find total unique paths in a grid.
"""
def countPathsTopDown(m, n):
    """
    TC - O(m * n)
    SC - O(path length) + O(m * n) = O((n - 1) + (m - 1)) + O(m * n)
    """
    def countPaths(row, col, dp):
        if row == 0 and col == 0:
            return 1
        
        if row < 0 or col < 0:
            return 0
        
        if dp[row][col] != -1:
            return dp[row][col]
        
        upward = countPaths(row - 1, col, dp)
        leftward = countPaths(row, col - 1, dp)

        dp[row][col] = upward + leftward
        return dp[row][col]
    
    dp = [[-1] * n for _ in range(m)]
    result = countPaths(m - 1, n - 1, dp)
    return result

def countPathsBottomUp(m, n):
    """
    TC - O(m * n)
    SC - O(m * n)
    """
    def countPaths(dp):
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                else:
                    upward = 0
                    leftward = 0
                    if i > 0:
                        upward = dp[i - 1][j]
                    if j > 0:
                        leftward = dp[i][j - 1]
                    dp[i][j] = upward + leftward
        return dp[m - 1][n - 1]
    
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    result = countPaths(dp)
    return result

def countPathsBottomUpOptimized(m, n):
    """
    TC - O(m * n)
    SC - O(n)
    """
    prev = [0] * n
    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = 1
            else:
                upward = 0
                leftward = 0
                if i > 0:
                    upward = prev[j]
                if j > 0:
                    leftward = temp[j - 1]
                temp[j] = upward + leftward
        prev = temp
    return prev[n - 1]

if __name__ == '__main__':
    m, n = 3, 3    # rows, columns
    # result = countPathsTopDown(m ,n)
    # result = countPathsBottomUp(m, n)
    result = countPathsBottomUpOptimized(m, n)
    print(result)