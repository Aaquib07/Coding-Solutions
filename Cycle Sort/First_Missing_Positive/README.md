# Problem
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

### Constraints
- 1 <= nums.length <= 10^5^
- -2^31^ <= nums[i] <= 2^31^ - 1

# Solution
## Approach 1 (TC: O(N), SC: O(N))
In this approach, we initialize a list of length 1 greater than the length of `nums` for lookup of every positive number. We set all the entries to be False initially as we haven't seen any of the positive numbers yet. Then we iterate through `nums` and mark the positive numbers as seen. Once we update the lookup list, we iterate through all positive numbers from 1 to length of `nums` and check if any of them is missing or not. If the number is missing, we return it. If all the positive number are seen, we return `len(nums) + 1`. 

### Code
```python
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)  # Lookup list

        # Mark the positive elements from nums
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        
        # Iterate thorugh positive numbers 1 to n
        for i in range(1, n + 1):
            # If the number is not seen, we return it
            if not seen[i]:
                return i
        
        # If all the positive numbers are seen, we return n + 1
        return n + 1


if __name__ == '__main__':
    nums = [1, 2, 0]
    result = Solution().firstMissingPositive(nums)
    print(result)
```

## Approach 2 (TC: O(N), SC: O(1))
In this approach, we use cycle sort to place the positive numbers smaller than the length of `nums` at the correct index. We iterate over `nums` and for each element we find its correct index on the number line (1 would be at index 0, 2 would be at index 1, 0 would be at index -1, and so on). Then we check if the element is positive (lies between 0 and length of `nums`) and whether the element at current index matches does not match with the element at the correct index, swapping in this case. Otherwise, we just increment the index. Then we iterate through the sorted `nums` to check whether the element at index `i` does not match `i + 1` (correct index), returning `i + 1` in this case. If all the numbers are at their correct index, we return `len(nums) + 1`.

**NOTE: This approach modifies the input**

**Code for this approach is given in the python file**