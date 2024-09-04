from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        def topdowm(index: int, prev_index: int) -> List[int]:
            # If length of array exceeded
            if index == n:
                return []
            
            # Return the result if it has been computed previously
            if (index, prev_index) in memo:
                return memo[(index, prev_index)]
            
            # Expand the longest subsequence without taking the current index element
            longest_subsequence = topdowm(index + 1, prev_index)
            
            # If no element is selected or element at prev_index exactly divides the element at current index
            if prev_index == -1 or nums[index] % nums[prev_index] == 0:
                # Add the current index element and recursively go to next index
                temp = [nums[index]] + topdowm(index + 1, index)
                # If a greater length subsequence is obtained
                if len(temp) > len(longest_subsequence):
                    # Update the longest subsequence
                    longest_subsequence = temp
            
            # Store the longest subsequence into our memo
            memo[(index, prev_index)] = longest_subsequence
            return memo[(index, prev_index)]
        

        n = len(nums)    # Length of array
        # Sort the array
        nums.sort()
        memo = {}
        return topdowm(0, -1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().largestDivisibleSubset(nums)
    print(result)
