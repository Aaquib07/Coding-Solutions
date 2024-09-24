# Problem
Given a set of distinct positive integers `nums`, return the largest subset answer such that every pair (`answer[i]`, `answer[j]`) of elements in this subset satisfies:

- `answer[i]` % `answer[j]` == 0, or
- `answer[j]` % `answer[i]` == 0

If there are multiple solutions, return any of them.

### Constraints
- 1 <= `nums.length` <= 1000
- 1 <= `nums[i]` <= 2 * 109
- All the integers in nums are **unique**.

# Solution
## Approach 1 $(TC: O(N^2), SC: O(N^2 + RecursionStackSpace))$
In this approach, we use a top down dynamic programming method. At first, we just the `nums` array so that we only have to check one out of two given conditions. Then we call a recursive function `topdown` that takes the current index and previous index as its parameters. The base case if when we reach the end of the array, returning an empty array in that case. Then we check if the computation for the pair (current index, previous index) has been done previously, if yes, we return the result. Otherwise, we expand the existing subsequence without considering the current index. Then we check, if no element has been considered (`prev_index == -1`) or previous index element divides current index element, then we consider the current index element and then expand the subsequence further. If this subsequence length exceeds the length of the subsequence that was expanded without considering the current index element, we just update the maximum length subsequence and store it in the memo. Lastly, we return the result.


### Code
```python
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
```

## Approach 2 $(TC: O(N^2), SC: O(N^2))$
In the previous approach, there is an additional stack space that we can optimize. So we use bottom up dynamic programming to avoid the addtional stack space. We again sort the array. We use a `dp` array that stores the subsequence ending with `nums[i]` at index `i`. We iterate over the indices followed by an iteration for the previous indices. If the current index element is divisible by previous index element, we update the longest subsequence. Lastly, we return the longest length subsequence.

### Code
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Length of the array
        n = len(nums)
        # Sort the array
        nums.sort()
        
        # Store the subsequence ending with nums[i] at index i
        dp = [[num] for num in nums]
        
        
        for index in range(1, n):
            for prev_index in range(index):
                # If the current index element is divisible by previous index element
                if nums[index] % nums[prev_index] == 0:
                    # Update the longest subsequence
                    if len(dp[prev_index]) + 1 > len(dp[index]):
                        dp[index] = dp[prev_index] + [nums[index]]
        
        # Return the longest length subsequence
        return max(dp, key=len)
```

## Approach 3 $(TC: O(N^2), SC: O(N))$
We can further optimize space if we consider only the indices and length of longest divisible subsequence instead of considering the whole subsequence at once. In this approach, we use a `dp` array that stores the length of longest divisible subsequence ending with `nums[i]`. Next, we use a `prev` array that stores the previous index of element in the longest divisible subsequence ending at `nums[i]`. We use a variable `max_index` that stores the ending index of longest divisible subsequence. Then we iterate through the array `nums` followed by the iteration for previous indices and check if the current index element is divisible by previous index element. If so, we update the length of longest divisible subsequence and the previous index of current element. Then we check for each current index, whether the length of longest divisible subsequence ending at current index is larger than that ending at `max_index`. If so, we update the `max_index`. After all the iterations get over, `max_index` contains the endin index of the longest divisible subsequence. So we just reconstruct the subsequence using `max_index` and `prev` (used to get the previous index of current max_index). Lastly, we return the reverse of the subsequence obtained to get it in ascending order. 

**Code for this approach is given in the python file**