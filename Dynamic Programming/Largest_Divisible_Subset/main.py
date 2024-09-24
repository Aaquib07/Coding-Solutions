from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Length of the array
        n = len(nums)
        # Sort the array
        nums.sort()
        # Stores the length of the longest divisible subsequence ending with nums[i]
        dp = [1] * n
        # Stores the index of previous element in the longest divisible subsequence ending at nums[i]
        prev = [-1] * n
        # Stores the index of the longest divisible subsequence
        max_index = 0

        for index in range(n):
            for prev_index in range(index):
                # If the current index element is divisible by previous index element
                if nums[index] % nums[prev_index] == 0:
                    # Update the length of longest divisible subsequence and the index of previous element w.r.t current index element
                    if dp[index] < dp[prev_index] + 1:
                        dp[index] = 1 + dp[prev_index]
                        prev[index] = prev_index
            
            # Update the max_index if a longer subsequence found
            if dp[index] > dp[max_index]:
                max_index = index
        
        # Stores the longest divisble subsequence
        result = []
        # Reconstruct the subsequence
        current = max_index
        while current != -1:
            result.append(nums[current])
            current = prev[current]
        
        # Return the result in ascending order
        return result[::-1]



if __name__ == '__main__':
    nums = [1, 2, 3]
    result = Solution().largestDivisibleSubset(nums)
    print(result)
