from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Hashmap to store count of distinct elements
        hashmap = defaultdict(int)
        # Stores the count of valid subarrays
        result = 0
        # Left pointer
        left = 0
        # Stores the count of subarrays with current
        # distinct elements
        current_count = 0
        
        # Iterate through nums using right pointer
        for right in range(len(nums)):
            # Increment the count of current element
            hashmap[nums[right]] += 1

            # If a new distinct element appears
            if hashmap[nums[right]] == 1:
                # Decrement k
                k -= 1
            
            # If k becomes negative, shrink the window
            if k < 0:
                # Decrement the count of left pointer element
                hashmap[nums[left]] -= 1
                # If the count becomes 0
                if hashmap[nums[left]] == 0:
                    # Increment k
                    k += 1
                # Increment the left pointer
                left += 1
                current_count = 0
            
            # If k becomes 0
            if k == 0:
                # Shrink the window further until count
                # of left pointer element becomes 1
                while hashmap[nums[left]] > 1:
                    # Decrement count of left pointer element
                    hashmap[nums[left]] -= 1
                    # Increment left pointer
                    left += 1
                    # Increment the count of subarrays with
                    # current distinct elements
                    current_count += 1

                # Update the result
                result += (current_count + 1)
        
        return result


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 3]
    k = 2
    result = Solution().subarraysWithKDistinct(nums, k)
    print(result)