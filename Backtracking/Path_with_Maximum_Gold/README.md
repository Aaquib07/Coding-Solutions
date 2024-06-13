# Problem
In a gold mine grid of size `m x n`, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:
- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold.

### Constraints
- m == `grid.length`
- n == `grid[i].length`
- 1 <= m, n <= 15
- 0 <= `grid[i][j]` <= 100
- There are at most 25 cells containing gold.

# Solution
## Approach (TC: O(G * 3<sup>G</sup>), SC: O(G))
#### G stands for the number of gold cells.

Since we can start from any cell in the grid to find out the maximum gold, so we iterate through each and every cell as the starting cell. For each cell, we check whether the cell lies inside the grid or whether the cell has been visited before, returning 0 in either cases. Otherwise, we just take the entire gold from the current cell. Then we perform backtracking by traversing the remaining 3 directions (not 4 directions because we can't go back to the cell that has been visited before). Lastly we return the result.

**Code for this approach is given in the python file**