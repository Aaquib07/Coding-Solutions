# Question
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Constraints
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1

# Solution

## Intuition
The brute force strategy is to use recursion technique but that would be very expensive approach as per the constraints. Instead, we can use dynamic programming to optimize our approach.
We can store the number of unique paths in an array to avoid reconsidering the same steps again and again.

## Approach (Top Down DP)
1. We initialize an array named dp of m x n dimension with all the values -1.
```python
m = len(obstacleGrid)
n = len(obstacleGrid[0])
dp = [[-1] * n for _ in range(m)]
```
2. We start from the bottom-right corner.
```python
result = findPath(m - 1, n - 1, dp)
```
3. We check whether the current cell contains an obstacle, returning 0 in that case.
```python
if row >= 0 and col >= 0 and obstacleGrid[row][col] == 1:
    return 0
```
4. We check if we reached the top-left corner, returning 1 in that case. This indicates we have found 1 unique path.
```python
if row == 0 and col == 0:
    return 1
``` 
5. If we get out of the grid, we return 0.
```python
if row < 0 or col < 0:
    return 0
```
6. If we have computed the procedure for the current cell in the earlier iterations, we return the stored value.
```python
if dp[row][col] != -1:
    return dp[row][col]
```
7. Otherwise, we can move in 2 possible directions - upward and leftward.
```python
upward = findPath(row - 1, col, dp)
leftward = findPath(row, col - 1, dp)
```
8. We store the total number of unique paths from bottom-right corner to the current cell obtained by going upward and leftward in the array and return it.
```python
dp[row][col] = upward + leftward
return dp[row][col]
```

## Approach (Bottom Up DP)
1. We initialize a dp array of m x n dimension.
```python
m = len(obstacleGrid)
n = len(obstacleGrid[0])
dp = [[-1] * n for _ in range(m)]
```
2. We start from the top-left corner and for each cell we check whether it contains an obstacle, storing 0 in that case.
```python
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            dp[i][j] = 0
```
3. We check whether the cell is the top-left corner, storing 1 in that case.
```python
        elif i == 0 and j == 0:
            dp[i][j] = 1
```
4. Otheriwse, we can move in 2 possible directions - leftward and upward.
```python
        else:
            upward = 0
            leftward = 0
            if i > 0:
                upward = dp[i - 1][j]
            if j > 0:
                leftward = dp[i][j - 1]
```
5. We store the total number of unique paths from top-left corner to the current cell obtained by moving in those directions.
```python
            dp[i][j] = upward + leftward
```
6. Lastly, we return the stored result for bottom-right corner.
```python
return dp[m - 1][n - 1]
```

## Intuition for Space-Optimized Bottom Up DP
As we observe that only the previous row is involved in the calculation for the current row value, so we can use a couple of 1-d dp arrays storing only the current row and previous row values.

## Approach
1. We initialize a 1-d dp array to store the previous row values with all the values initially set to 0.
```python
prev = [0] * n
```
2. We iterate through all the rows, and for every row we initialize another 1-d dp array to store the current row value.
```python
for i in range(m):
    temp = [0] * n
```
3. We check if the cell (row, col) contains an obstacle, we set temp[col] to 0 as we cannot find any path.
```python
    for j in range(n):
        if grid[i][j] == 1:
            temp[j] = 0
```
4. If the cell is the starting cell, we set temp[col] to 1 as we found a path.
```python
        elif i == 0 and j == 0:
            temp[j] = 1
```
5. We take the previous row value and current row value at index column - 1 to calculate number of paths for temp[col].
```python
        else:
            upward = 0
            leftward = 0
            if i > 0:
                upward = prev[j]
            if j > 0:
                leftward = temp[j - 1]
            temp[j] = upward + leftward
```
6. We pass the values of the current rows to the previous rows for next iteration.
```python
    prev = temp
```
7. Lastly we return the number of unique paths to reach bottom-right cell.
```python
return prev[n - 1]
```