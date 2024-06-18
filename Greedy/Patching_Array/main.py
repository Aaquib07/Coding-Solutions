from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Initialize missing sum to 1
        missing_sum = 1
        # Stores the number of patches
        result = 0
        index = 0

        # Iterate until missing sum becomes greater than n
        while missing_sum <= n:
            # If the current number is less or equal to missing sum
            if index < len(nums) and nums[index] <= missing_sum:
                # Include the number in the missing sum
                missing_sum += nums[index]
                # Increment the index
                index += 1
            else:
                # Otherwise, add an additional number equal to the 
                # gap between the current number and missing sum
                missing_sum += missing_sum
                # Increment the result
                result += 1
        
        return result


if __name__ == '__main__':
    nums = [1, 5, 10]
    n = 20
    result = Solution().minPatches(nums, n)
    print(result)
