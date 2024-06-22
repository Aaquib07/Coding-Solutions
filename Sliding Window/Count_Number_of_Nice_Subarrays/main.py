from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def sliding_window(x: int):
            # Stores the number of subarrays having at most x odd numbers 
            result = 0
            # Initialize left pointer
            left = 0
            # Stores the count of odd numbers
            count = 0

            # Iterate through the list using right pointer
            for right in range(len(nums)):
                # If the number is odd
                if nums[right] % 2:
                    # Increment the count
                    count += 1
                
                # Shrink the window if count exceeds x
                while count > x:
                    # If number at the left index is odd
                    if nums[left] % 2:
                        # Decrement the count
                        count -= 1
                    # Increment the left pointer
                    left += 1
                
                # Update the result
                result += right - left + 1
            
            return result

        # Exact k odd numbers = at most k odd numbers - at most (k - 1) odd numbers
        return sliding_window(k) - sliding_window(k - 1)


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    result = Solution().numberOfSubarrays(nums, k)
    print(result)
