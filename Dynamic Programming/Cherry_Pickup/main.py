from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        for c2 in range(n):
            dp[n - 1][n - 1][n - 1] = grid[n - 1][n - 1]
        
        for r1 in range(n - 2, -1, -1):
            for c1 in range(n - 2, -1, -1):
                for c2 in range(n - 2, -1, -1):
                    r2 = r1 + c1 - c2
                    if r1 < 0 or r1 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        dp[r1][c1][c2] = float('-inf')
                        continue

                    cherry = grid[r1][c1]
                    if c1 != c2 or r1 != r2:
                        cherry += grid[r2][c2]
                    
                    
                    right1_down2 = dp[r1][c1 + 1][c2]
                    down1_right2 = dp[r1 + 1][c1][c2 + 1]
                    right1_right2 = dp[r1][c1 + 1][c2 + 1]
                    down1_dowm2 = dp[r1 + 1][c1][c2]

                    dp[r1][c1][c2] = cherry + max(right1_down2, down1_right2, right1_right2, down1_dowm2)
        
        return dp
    


if __name__ == '__main__':
    # grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
    result = Solution().cherryPickup(grid)
    print(result)