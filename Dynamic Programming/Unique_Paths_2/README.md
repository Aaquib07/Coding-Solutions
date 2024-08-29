# Question
You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Constraints
- m == `obstacleGrid.length`
- n == `obstacleGrid[i].length`
- 1 <= m, n <= 100
- `obstacleGrid[i][j]` is 0 or 1

# Solution

## Approach 1 $(TC: O(M \cdot N ), SC: O(M \cdot N + Recursion Stack Space))$
In this approach, we just want to explore all the possibilities. So, we take the help of recursion. But due to the strict constraints, we have to think of optimized solution. As we can observe, this problem involves overlapping subproblems. So, dynamic programming comes into the picture. So, we initialize a 2-d array `dp`. `dp[i][j]` tells use the number of ways in which we can reach cell (i, j) starting from cell (m - 1, n - 1). Now, we travel from cell (m - 1, n - 1) to each cell recursively in two directions - up and left. If the cell being visited is an obstacle, then there is no way we can reach the cell (0, 0). Next, we check if the current cell if the target cell (0, 0), returning 1 in this case (because we have found a way). If the robot goes out of bound, then again there is no ways. We check if we have computed the no. of ways for the cell, if yes, then we return it. Lastly, we just sum the number of ways by travelling in those two directions and store it in the `dp` array.

### Code
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        def findPath(row: int, col: int) -> int:
            # If the cell contains an obstacle
            if row >= 0 and col >= 0 and obstacleGrid[row][col] == 1:
                return 0

            # If the starting cell is reached
            if row == 0 and col == 0:
                return 1
            
            # If the robot goes out of bound
            if row < 0 or col < 0:
                return 0

            # If the number of ways for the cell has already been computed
            if dp[row][col] != -1:
                return dp[row][col]
            
            # Robot goes in the upward direction
            upward = findPath(row - 1, col)
            # Robot goes in the left direction
            leftward = findPath(row, col - 1)

            # Add the number of ways found from both directions
            dp[row][col] = upward + leftward
            return dp[row][col]


        m = len(obstacleGrid)    # No. of rows
        n = len(obstacleGrid[0])    # No. of columns
        # Stores the number of ways to reach any cell in the grid from (m - 1, n - 1) cell
        dp = [[-1] * n for _ in range(m)]
        result = findPath(m - 1, n - 1, dp)
        return result
```