# Problem
You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s (representing water) and `1`'s (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in `grid2` is considered a sub-island if there is an island in `grid1` that contains all the cells that make up this island in `grid2`.

Return the number of islands in `grid2` that are considered sub-islands.

### Constraints
- m == `grid1.length` == `grid2.length`
- n == `grid1[i].length` == `grid2[i].length`
- 1 <= m, n <= 500
- `grid1[i][j]` and `grid2[i][j]` are either 0 or 1.

# Solution
## Approach $(TC: O(M \cdot N), SC: O(M \cdot N))$
We initialized a 2-d array `visited` that keeps track of the status of the cell in the grid (i.e., whether the cell has been visited before or not). Initially, all the cells in `grid2` are not visited so we initialize the `visited` array with all the values set to False. Next, we traverse through each cell of `grid2` and increment the number of sub-islands if the following three conditions are satisfied:

- If the cell is a land.
- If the cell has not been visited previously.
- If the cell is a part of sub-island (This check is done through a BFS (Breadth First Search) traversal algorithm)

Now, a BFS traversal has been done to find out whether an island is a sub-island or not (We can also use DFS traversal as an alternative). In this approach, we define a variable `subIsland` to indicate whether an island in `grid2` is a sub-island or not. Then, we initialize a queue to store all the cells to process. If the corresponding cell in `grid1` is not a land cell, then we just set the `subIsland` to False to indicate that the island being considered currently is not a sub-island. Then, we just travel through all the four neighbors of the cell and just make sure that the new cell is a valid one and then add the new cell to the queue and set the new cell as visited.

**Code for this approach is given in the python file**