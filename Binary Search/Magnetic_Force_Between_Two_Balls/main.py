from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Stores the maximum distance
        result = 0
        # Length of position list
        n = len(position)
        # Sort position list
        position.sort()

        # Initialize left pointer
        left = 1
        # Initialize right pointer
        right = max(position) // (m - 1) + 1

        # Until left pointer does not exceed right pointer
        while left <= right:
            # Initialize mid pointer
            mid = (left + right) // 2
            
            # Previous ball position
            previous_ball = position[0]
            
            # Stores the number of balls placed
            balls_placed = 1

            # Indicates whether all the balls can be placed or not
            can_be_placed = False

            # Iterate through every position
            for i in range(1, n):
                # Current poisiton
                curr_position = position[i]
                # If ball can be placed at the current position
                if curr_position - previous_ball >= mid:
                    # Increment the no. of placed balls
                    balls_placed += 1
                    # Update previous ball position to the current position
                    previous_ball = curr_position
                
                # If all the balls have been placed
                if balls_placed == m:
                    can_be_placed = True
                    break
            
            if can_be_placed:
                # Update the maximum distance as the mid pointer value
                result = mid
                # Update the left pointer
                left = mid + 1
            else:
                # Otherwise, update the right pointer
                right = mid - 1
        
        return result




if __name__ == '__main__':
    position = [1, 2, 3, 4, 7]
    m = 3
    result = Solution().maxDistance(position, m)
    print(result)
