from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []  # Stores the duplicates

        # Iterate thorugh the list
        for num in nums:
            # If the element at index abs(num) - 1 is negative
            # (this means abs(num) has occurred before)
            if nums[abs(num) - 1] < 0:
                # Add the absolute value of element to our result
                result.append(abs(num))
            else:
                # Otherwise, mark the element at index abs(num) - 1 as negative
                nums[abs(num) - 1] *= -1
        
        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDuplicates(nums)
    print(result)