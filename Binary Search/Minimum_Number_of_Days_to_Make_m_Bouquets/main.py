from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # If the no. of flowers is not sufficient
        if len(bloomDay) < m * k:
            # It is impossible
            return -1
        
        # Stores the minimum no. of days
        result = -1
        # Initialize left pointer
        left = 0
        # Initialize right pointer
        right = max(bloomDay)

        # Until left pointer is less than or equal to the right pointer
        while left <= right:
            # Initialize mid
            mid = (left + right) // 2
            # Stores the count of adjacent bloomed flowers
            count = 0
            # Stores the no. of bouquets
            bouquets = 0

            # Iterate through every bloom day
            for day in bloomDay:
                # If the day is less than or equal to mid
                # that means the flower is already bloomed
                if day <= mid:
                    # Increment count
                    count += 1
                else:
                    # Otherwise, reset the count to 0
                    count = 0
                
                # If the no. of adjacent bloomed flowers equals k
                if count == k:
                    # Increment no. of bouquets
                    bouquets += 1
                    # Reset the count to 0
                    count = 0
            
            # If no. of bouquets are sufficient
            if bouquets >= m:
                # Update result
                result = mid
                # Update the right pointer to search in the left half
                right = mid - 1
            else:
                # Otherwise, update the left pointer to search in the right half
                left = mid + 1
        
        return result
    

if __name__ == '__main__':
    blooomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    result = Solution().minDays(blooomDay, m, k)
    print(result)
    
