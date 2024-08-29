from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])

        dp = [[0] * columns for _ in range(rows)]

        for row in range(rows):
            dp[row][0] = matrix[row][0]
        
        for col in range(columns):
            dp[0][col] = matrix[0][col]
        
        for row in range(1, rows):
            for col in range(1, columns):
                if matrix[row][col] == 1:
                    up = dp[row - 1][col]
                    left = dp[row][col - 1]
                    up_left = dp[row - 1][col - 1]
                    dp[row][col] = 1 + min(up, left, up_left)
        
        result = 0
        for row in range(rows):
            for col in range(columns):
                result += dp[row][col]
        
        return result