from typing import List

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
    


if __name__ == '__main__':
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    result = Solution().cherryPickup(grid)
    print(result)