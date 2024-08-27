from typing import List
from collections import deque

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def floodFill(modified_grid: List[List[int]], row: int, col: int):            
            if row < 0 or row >= len(modified_grid) or col < 0 or col >= len(modified_grid) or modified_grid[row][col] != 0:
                return
            
            modified_grid[row][col] = 1
            floodFill(modified_grid, row + 1, col)
            floodFill(modified_grid, row - 1, col)
            floodFill(modified_grid, row, col + 1)
            floodFill(modified_grid, row, col - 1)


        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        n = len(grid)
        modified_grid = [[0 for _ in range(n * 3)] for _ in range(n * 3)]
        grid = [list(ch) for ch in grid]

        for i in range(n):
            for j in range(n):
                curr_row = i * 3
                curr_col = j * 3

                if grid[i][j] == '\\':
                    modified_grid[curr_row][curr_col] = 1
                    modified_grid[curr_row + 1][curr_col + 1] = 1
                    modified_grid[curr_row + 2][curr_col + 2] = 1
                elif grid[i][j] == '/':
                    modified_grid[curr_row][curr_col + 2] = 1
                    modified_grid[curr_row + 1][curr_col + 1] = 1
                    modified_grid[curr_row + 2][curr_col] = 1

        
        result = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if modified_grid[i][j] == 0:
                    floodFill(modified_grid, i, j)
                    result += 1
        
        return result



if __name__ == '__main__':
    grid = ['/\\', '\\/']
    result = Solution().regionsBySlashes(grid)
    print(result)