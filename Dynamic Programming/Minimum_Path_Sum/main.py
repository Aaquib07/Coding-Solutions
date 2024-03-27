def minSumPathTopDown(n, m, grid):
    """
    TC - O(n * m)
    SC - O(n * m) + O(path length)
    """
    def findPath(row, col, dp):
        if row == 0 and col == 0:
            return grid[row][col]
        
        if row < 0 or col < 0:
            return float('inf')
        
        if dp[row][col] != -1:
            return dp[row][col]

        upward = grid[row][col] + findPath(row - 1, col, dp)
        leftward = grid[row][col] + findPath(row, col - 1, dp)

        dp[row][col] = min(upward, leftward)
        return dp[row][col]
    
    dp = [[-1] * m for _ in range(n)]
    result = findPath(n - 1, m - 1, dp)
    return result

def minSumPathBottomUp(n, m, grid):
    """
    TC - O(n * m)
    SC - O(n * m)
    """
    def findPath(dp):
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                else:
                    upward = grid[row][col]
                    leftward = grid[row][col]
                    if row > 0:
                        upward += dp[row - 1][col]
                    else:
                        upward += float('inf')
                    if col > 0:
                        leftward += dp[row][col - 1]
                    else:
                        leftward += float('inf')
                    dp[row][col] = min(upward, leftward)
        return dp[n - 1][m - 1]
    
    dp = [[-1] * m for _ in range(n)]
    result = findPath(dp)
    return result

def minSumPathBottomUpOptimized(n, m, grid):
    """
    TC - O(n * m)
    SC - O(m)
    """
    prevRow = [0] * m
    for row in range(n):
        currRow = [0] * m
        for col in range(m):
            if row == 0 and col == 0:
                currRow[col] = grid[row][col]
            else:
                upward = grid[row][col]
                leftward = grid[row][col]
                if row > 0:
                    upward += prevRow[col]
                else:
                    upward += float('inf')
                if col > 0:
                    leftward += currRow[col - 1]
                else:
                    leftward += float('inf')
                currRow[col] = min(upward, leftward)
        prevRow = currRow
    return prevRow[m - 1]

if __name__ == '__main__':
    grid = [
        [10, 4, 100],
        [6, 1, 1],
        [3, 2, 4],
    ]
    n, m = 3, 3
    # result = minSumPathTopDown(n, m, grid)
    # result = minSumPathBottomUp(n, m, grid)
    result = minSumPathBottomUpOptimized(n, m, grid)
    print(result)