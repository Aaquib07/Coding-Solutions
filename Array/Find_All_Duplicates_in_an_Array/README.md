# Problem
Given an integer array `nums` of length `n` where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

### Constraints
- n == `nums.length`
- 1 <= n <= 10<sup>5</sup>
- 1 <= `nums[i]` <= n

# Solution
## Approach 1 $(TC: O(N), SC: O(N))$
In this approach, we use a hashmap to store the frequencies of elements in the list. Then we iterate through the list and update the frequency of element in the hashmap. Once the hashmap is updated, we iterate over the hashmap and check the frequencies of the elements. If the frequency of an element is greater than 1, we add the element into our result. 

### Code
```python
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Hashmap to store the frequency of elements
        freq_map = {}
        
        # Iterate through the list
        for num in nums:
            # Update the frequency of elements in hashmap
            freq_map[num] = freq_map.get(num, 0) + 1
        
        result = []  # Stores the duplicates
        # Iterate thorugh the hashmap
        for num, freq in freq_map.items():
            # If frequency of the element is greater than 1
            if freq > 1:
                # Add the element in our result
                result.append(num)
        
        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDuplicates(nums)
    print(result)
```

## Approach 2 $(TC: O(N), SC: O(1))$
In this approach, we take the advantage of the fact that the elements lies between 1 and `n`. We just iterate through the list and mark the element at index `abs(current_element) - 1` as negative to indicate that it has occurred. If we ever find that the element at index `abs(current_index) - 1` is negative that means the current element has occurred previously that led to the element at index `abs(current_index) - 1` being negative. So we just add the absolute value of current element to our result.

**Code for this approach is given in the python file**