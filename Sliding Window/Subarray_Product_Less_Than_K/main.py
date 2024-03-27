from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge case when no subarrays are possible
        if k <= 1:
            return 0
        
        result = 0  # Stores the total count of subarrays
        product = 1  # Stors the product

        # Initialize left pointer at 0-th index
        left = 0
        # Iterate using right pointer
        for right in range(len(nums)):
            # Expand the window by including the right pointer element
            product *= nums[right]

            # Shrink the window from the left until the product becomes
            # less than k
            while product >= k:
                # Remove the element at the left pointer from product
                product //= nums[left]
                # Increment left pointer
                left += 1
            
            # Update the total count by adding number of valid subarrays
            result += right - left + 1
        
        return result



if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)