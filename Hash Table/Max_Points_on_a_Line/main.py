from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Stores the count of points
        result = 0

        # Iterate through every point
        for p1 in points:
            # Hashmap to store the number of points having a particular slope
            slope_map = {}
            # Count of same points
            same_points = 0
            # Maximum count of all slopes
            max_count = 0

            # Iterate through every point
            for p2 in points:
                # If both points are same
                if p1 == p2:
                    # Increment same_points
                    same_points += 1
                    continue
                
                # Otherwise, get the x-coordinates of both points
                x1, x2 = p1[0], p2[0]
                # If the x-coordinates are same
                if x1 == x2:
                    # Slope will be infinite
                    slope = float('inf')
                else:
                    # Otherwise, get the y-coordinates of both points
                    y1, y2 = p1[1], p2[1]
                    # Calculate the slope
                    slope = (y1 - y2) / (x1 - x2)
                
                # Update the count of the slope
                slope_map[slope] = slope_map.get(slope, 0) + 1
                # Update the max count of slopes
                max_count = max(max_count, slope_map[slope])
            
            # Update the result
            result = max(result, max_count + same_points)
        
        return result



if __name__ == '__main__':
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    result = Solution().maxPoints(points)
    print(result)
