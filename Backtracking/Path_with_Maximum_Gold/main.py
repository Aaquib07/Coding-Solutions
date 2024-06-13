from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs_backtrack(row: int, col: int):
            # Base case (either the cell does not lie inside the grid or it has no gold)
            if row < 0 or col < 0 or row == rows or col == columns or grid[row][col] == 0:
                return 0
            
            max_gold = 0    # Stores the maximum gold that can be obtained
            # Save the value of the cell
            original = grid[row][col]
            # Take all the gold from the cell
            grid[row][col] = 0

            # Traverse in up, down, right, left directions
            for dr, dc in DIRECTIONS:
                # Update the max_gold value
                max_gold = max(max_gold, dfs_backtrack(row + dr, col + dc))
            
            # Set the value of the cell as the original value
            grid[row][col] = original
            return max_gold + grid[row][col]

            
        rows = len(grid)
        columns = len(grid[0])
        DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]    # (up, down, right, left)
        max_gold = 0

        # Start traversing from each cell to obtain the max gold
        for row in range(rows):
            for col in range(columns):
                max_gold = max(max_gold, dfs_backtrack(row, col))
        
        return max_gold


if __name__ == '__main__':
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    result = Solution().getMaximumGold(grid)
    print(result)