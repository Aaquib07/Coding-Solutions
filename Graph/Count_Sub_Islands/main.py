from typing import List
from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def checkSubIsland(row: int, col: int) -> bool:
            # Stores whether the cell is a sub-island cell or not (initially set to True)
            subIsland = True
            # Queue to store the cells to visit
            queue = deque()
            queue.append((row, col))
            # Mark the cell as visited
            visited[row][col] = True

            while queue:
                currRow, currCol = queue.popleft()

                # If the correspnding cell in grid 1 is not land
                if grid1[currRow][currCol] == 0:
                    # Cell is not a sub-island cell
                    subIsland = False

                # Traverse in all the 4 directions
                for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newRow, newCol = currRow + drow, currCol + dcol

                    # If the new cell is within the boundary of the grid 2 and it is a land and it has not been visited previously
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid2[newRow][newCol] == 1 and not visited[newRow][newCol]:
                        # Add the new cell to the queue
                        queue.append((newRow, newCol))
                        # Mark the new cell as visited
                        visited[newRow][newCol] = True
            
            return subIsland


        rows = len(grid2)
        cols = len(grid2[0])
        # Keeps track of whether a grid cell has been seen before
        visited = [[False] * cols for _ in range(rows)]
        # Stores the count of sub-islands
        result = 0

        # Iterate through every cell of grid 2
        for i in range(rows):
            for j in range(cols):
                # If the cell is a land and it has not been seen before and it is a sub-island cell
                if grid2[i][j] == 1 and not visited[i][j] and checkSubIsland(i, j):
                    # Increment the count
                    result += 1
        
        return result



if __name__ == '__main__':
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    result = Solution().countSubIslands(grid1, grid2)
    print(result)
