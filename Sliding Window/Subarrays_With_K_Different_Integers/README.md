# Problem
Given an integer array `nums` and an integer `k`, return the number of good subarrays of nums.
- A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

### Constraints
- 1 <= nums.length <= 2 * 10^4^
- 1 <= nums[i], k <= nums.length

# Solution
## Approach 1 (TC: O(N), SC: O(N))
We intialize a hashmap to store the count of distinct element in `nums`. Since our focus is on subarrays, we can use sliding window to keep an eye on all the subarrays. So, we initialize left pointer (`left`) and right pointer (`right`) at index 0 and start iterating using right pointer. Left pointer corresponds to start of window and right pointer corresponds to end of window. 

While expanding the window, we increment the count of the current element (`nums[right]`). If the count of distinct elements goes beyond `k`, we start shrinking the window until the count of distinct elements becomes `k` again. While shrinking the window, we decrement the count of left pointer element (`nums[left]`). if the count of left pointer element becomes 0, we just delete the entry from our hashmap. Then we increment the left pointer. We update the count of good subarrays by adding the length of the current valid window (`right - left + 1`).

**Why are we using `right - left + 1`?** As we know, it gives the count of all the subarrays ending at index `right`. Additionally, in this case, it gives us the count of subarrays having at most `k` distinct elements.
We again go through the same process for k - 1. This will give us the count of subarrays having at most `k - 1` distinct elements. Let's call this process A (with k - 1) and the above process B (with k). Finally, we subtract A from B to get the desired result. 

### Code
```python
from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def slidingWindow(nums, k):
            # Hashmap to store count of elements
            hashmap = defaultdict(int)
            # Stores the number of subarrays having at most k distinct elements
            result = 0
            # Left pointer
            left = 0
            
            # Iterate through the right pointer (expand the window)
            for right in range(len(nums)):
                # Update the count of element
                hashmap[nums[right]] += 1

                # Shrink the window if distinct elements exceeds k
                while len(hashmap) > k:
                    # Decrement count of left pointer element
                    hashmap[nums[left]] -= 1
                    # If the count becomes 0
                    if hashmap[nums[left]] == 0:
                        # Delete the entry
                        del hashmap[nums[left]]
                    # Increment the left pointer
                    left += 1
                
                # Update the result
                result += right - left + 1  
            
            return result
        
        # Subtract count of subarrays with atmost k - 1 distinct elements from 
        # count of subarrays with atmost k distinct elements 
        exactly_k_distinct_element_subarrays = slidingWindow(nums, k) - slidingWindow(nums, k - 1)
        return exactly_k_distinct_element_subarrays


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 3]
    k = 2
    result = Solution().subarraysWithKDistinct(nums, k)
    print(result)
```

## Approach 2 (TC: O(N), SC: O(N))
In this approach, we still use sliding window approach but we just perform one pass. Similar to the above approach, we initialize a hashmap to store the count of distinct elements of `nums`. We intialize a left pointer and a right pointer at index 0. We initialize a variable `current_count` to store the count of subarrays with the current distinct elements. 

While expanding the window, we increment the count of the current element. If a new distinct element appears, we decrement `k`. If `k` becomes negative, then it means there are more than `k` distinct elements in the window, so we need to shrink it. While shrinking, we decrement the count of element at left pointer. If the count of element at left pointer becomes 0, that means there are again exactly `k` elements in the window, so we increment `k`. Then increment the left pointer and reset `current_count` to 0. If `k` becomes 0, that means we have `k` elements inside the window but we can still possibly shrink the window as some duplicates can be present. So, we shrink the window until the count of left pointer element becomes 1. While shrinking, we again decrement the count of left pointer element and increment the left pointer. This time we also increment the `current_count` by 1. Lastly we update the result by adding `current_count + 1`. Additional 1 is needed as because we need to count the current window as well as the possible windows inside it.

**Code for this approach is given in the python file**