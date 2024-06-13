from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, columns = len(matrix), len(matrix[0])
        heights = [0] * columns
        max_rectangle = 0

        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            max_rectangle = max(max_rectangle, self.largestAreaRectangle(heights))
        
        return max_rectangle
    
    def largestAreaRectangle(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                current_height = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, width * heights[current_height])
        
        while stack:
            current_height = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, width * heights[current_height])
        
        return max_area


if __name__ == '__main__':
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0'],
    ]
    result = Solution().maximalRectangle(matrix)
    print(result)