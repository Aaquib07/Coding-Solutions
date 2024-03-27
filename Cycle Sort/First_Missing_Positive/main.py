from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        n = len(nums)
        # Cycle sort to place positive elements smaller than n
        # at the correct index
        while index < n:
            correct_index = nums[index] - 1
            if 0 < nums[index] <= len(nums) and nums[index] != nums[correct_index]:
                # Swap if the positive element is not at the correct index
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
            else:
                # Increment the index
                index += 1

        for i in range(n):
            # If the positive number does not match its correct index,
            # we return it
            if nums[i] != i + 1:
                return i + 1
        
        # If all elements are at the correct index then the smallest
        # missing positive number is n + 1
        return n + 1


if __name__ == '__main__':
    nums = [1, 2, 0]
    result = Solution().firstMissingPositive(nums)
    print(result)