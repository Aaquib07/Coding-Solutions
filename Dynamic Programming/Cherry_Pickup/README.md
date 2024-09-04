# Problem
You are given an `n x n` grid representing a field of cherries, each cell is one of three possible integers.

- 0 means the cell is empty, so you can pass through,
- 1 means the cell contains a cherry that you can pick up and pass through, or
- -1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

- Starting at the position `(0, 0)` and reaching `(n - 1, n - 1)` by moving right or down through valid path cells (cells with value 0 or 1).
- After reaching `(n - 1, n - 1)`, returning to `(0, 0)` by moving left or up through valid path cells.
- When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `0`.
- If there is no valid path between `(0, 0)` and `(n - 1, n - 1)`, then no cherries can be collected.

### Constraints
- n == `grid.length`
- n == `grid[i].length`
- 1 <= n <= 50
- `grid[i][j]` is -1, 0, or 1.
- `grid[0][0]` != -1
- `grid[n - 1][n - 1]` != -1

# Solution
## Approach 1 $(TC: O(N^3), SC: O(N^3))$
In this approach, we use a top-dowm dynamic programming method. As we observe in this problem, there is a scenario of overlapping subproblems; and that's why we used dynamic programming. Initially, we define a `memo` that stores the number of cherries collected will cell (i, j) starting from cell (0, 0). Also, we changed our perspective for 2nd round of traversal from cell (n - 1, n - 1) to (0, 0). Instead of traversing in that sense, we traverse again from (0, 0) to (n - 1, n - 1) to make our computation simple to perform. As we perform 2 traversals at the same time from (0, 0), we should have taken 4 parameters `(r1, c1, r2, c2)` (as because these would change over time). But if we observe, every time the `r + c` value for any cell `(r, c)` would be the same. That is why, we can express `r2` in terms of `r1`, `c1` and `c2` as `r2 = r1 + c1 - c2`. Hence, we only need to track 3 parameters.

Now we start from traversing from cell (0, 0). Every time we traverse to a cell, we check if we have reached the cell (n - 1, n - 1). If we have reached, then we just collect the cherries in that cell. Moreover, if we ever exceed the grid boundary or if the cell contains a thorn, we can never get to the target cell (n - 1, n - 1). Then, we collect the cherries in the current cell and then check if both traversals lead to the same cell or not. If not, then we add the cherries from the other traversal as well. Next, we traverse in 4 possible directions:

- going right in traversal 1 and going dowm in traversal 2 
- going right in traversal 1 and going right in traversal 2 
- going dowm in traversal 1 and going right in traversal 2 
- going dowm in traversal 1 and going dowm in traversal 2 

We just take the maximum cherries obtained out of these traversals and add it the current cherries and then store the value in our memo. Lastly, we return the result.

### Code
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        def topdown(r1: int, c1: int, c2: int) -> int:
            # Determine r2 with the help of r1, c1 and c2
            # At any instant row + col is same for both traversal
            r2 = r1 + c1 - c2
            # If the (n - 1, n - 1) cell is reached
            if r1 == n - 1 and c1 == n - 1:
                # Pickup the cherry
                return grid[r1][c1]
            
            # If the current cell in either of the traversals contains a thorn or boundary overflow occurred
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            # If the computation for the cell has been done previously, return it
            if memo[r1][c1][c2] != -1:
                return memo[r1][c1][c2]
            
            cherry = grid[r1][c1]
            # Add the cherries from both traversals if the cells are different
            if c1 != c2:
                cherry += grid[r2][c2]
            
            # Recursively traverse in all the possible directions
            right1_down2 = topdown(r1, c1 + 1, c2)
            down1_right2 = topdown(r1 + 1, c1, c2 + 1)
            right1_right2 = topdown(r1, c1 + 1, c2 + 1)
            down1_dowm2 = topdown(r1 + 1, c1, c2)

            # Store the current cherry count and max of the possibilities into the memo
            memo[r1][c1][c2] = cherry + max(right1_down2, down1_right2, right1_right2, down1_dowm2)
            # Return the result
            return memo[r1][c1][c2]

        n = len(grid)    # No. of rows and columns
        # Stores the count of cherries starting from cell (0, 0) till (r1, c1) and (r2, c2)
        memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        return max(0, topdown(0, 0, 0))
```