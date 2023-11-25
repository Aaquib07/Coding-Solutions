def mazeObstaclesTopBottom(n, m, grid):

    def findPath(row, col, dp):
        if row >= 0 and col >= 0 and grid[row][col] == 1:
            return 0

        if row == 0 and col == 0:
            return 1
        
        if row < 0 or col < 0:
            return 0

        if dp[row][col] != -1:
            return dp[row][col]
        
        upward = findPath(row - 1, col, dp)
        leftward = findPath(row, col - 1, dp)

        dp[row][col] = upward + leftward
        return dp[row][col]
    
    dp = [[-1] * n for _ in range(m)]
    result = findPath(m - 1, n - 1, dp)
    return result

def mazeObstaclesBottomUp(n, m, grid):

    def findPath(dp):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0

                elif i == 0 and j == 0:
                    dp[i][j] = 1

                else:
                    upward = 0
                    leftward = 0
                    if i > 0:
                        upward = dp[i - 1][j]
                    if j > 0:
                        leftward = dp[i][j - 1]

                    dp[i][j] = upward + leftward
        return dp[m - 1][n - 1]
    
    dp = [[-1] * n for _ in range(m)]
    result = findPath(dp)
    return result

def mazeObstaclesBottomUpOptimized(n, m, grid):
    prev = [0] * n
    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if grid[i][j] == 1:
                temp[j] = 0

            elif i == 0 and j == 0:
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
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    m, n = 3, 3
    # result = mazeObstaclesTopBottom(n, m, grid)
    # result = mazeObstaclesBottomUp(n, m, grid)
    result = mazeObstaclesBottomUpOptimized(n, m, grid)
    print(result)
