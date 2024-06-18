from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []    # Stores the resulting triplets

        # Sort the nums list
        nums.sort()

        # Iterate through every index
        for i in range(n):
            # If the index is greater than 0 and current and previous element are same
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize left pointer
            left = i + 1
            # Initialize right pointer
            right = n - 1

            # Iterate until both pointers meet
            while left < right:
                # Total sum
                total_sum = nums[i] + nums[left] + nums[right]

                # If total sum is positive
                if total_sum > 0:
                    # Decrement right pointer
                    right -= 1
                # If total sum is negative
                elif total_sum < 0:
                    # Increment left pointer
                    left += 1
                else:
                    # Otherwise, add the triplet into the result
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    # Increment left pointer
                    left += 1

                    # Check for duplicate elements
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, 4]
    result = Solution().threeSum(nums)
    print(result)
