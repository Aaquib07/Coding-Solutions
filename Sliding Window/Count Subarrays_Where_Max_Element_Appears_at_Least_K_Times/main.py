from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0    # Stores the count of subarrays
        max_element = max(nums)    # Maximum element in nums
        max_element_count_in_window = 0    # Count of maximum element in window
        left = 0    # Left pointer (start of window)

        # Iterate through nums using right pointer
        for right in range(len(nums)):
            # If the element is the max_element
            if nums[right] == max_element:
                # Increment the count of max_element in the window
                max_element_count_in_window += 1
            
            # Shrink the window until count of max_element in the window goes below k
            while max_element_count_in_window == k:
                # If the start element of the window is the max_element
                if nums[left] == max_element:
                    # Decrement the count of max_element in the window
                    max_element_count_in_window -= 1
                # Increment the left pointer
                left += 1
            
            # Add the starting position of all the valid subarrays
            # (Left pointer goes through all the possible start position of the valid subarrays)
            result += left
        
        return result


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 3]
    k = 2
    result = Solution().countSubarrays(nums, k)
    print(result)