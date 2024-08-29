from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        m = len(obstacleGrid)    # No. of rows
        n = len(obstacleGrid[0])    # No. of columns

        # Stores the no. of ways of reaching any cell starting from cell (0, 0)
        dp = [[-1] * n for _ in range(m)]

        # Iterate through every cell from (0, 0)
        for i in range(m):
            for j in range(n):
                # If the cell contains an obstacle
                if obstacleGrid[i][j] == 1:
                    # There is no ways
                    dp[i][j] = 0
                # If cell (0, 0) is reached
                elif i == 0 and j == 0:
                    # Found a way
                    dp[i][j] = 1
                # Otherwise, add the number of ways returned from left and up directions
                else:
                    upward = 0
                    leftward = 0
                    if i > 0:
                        upward += dp[i - 1][j]
                    if j > 0:
                        leftward += dp[i][j - 1]
                    dp[i][j] = upward + leftward
        
        # Return the no. of ways of reaching cell (m - 1, n - 1)
        return dp[m - 1][n - 1]




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
