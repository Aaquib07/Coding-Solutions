# Problem
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

### Constraints
- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>4</sup> <= `nums[i]` <= 10<sup>4</sup>
- 1 <= k <= nums.length

# Solution
## Approach 1 $(TC: O(N \log K), SC: O(K))$
We start by creating a max heap that will store pairs of values from the array nums. Each pair consists of the negative value of an element (since Python’s heapq is a min-heap, we use negative values to simulate a max heap) and its index in the array. We fill the heap with the first k elements from the array. This represents the first window. The root of the heap contains the maximum value of the first window (remember, it’s stored as a negative number, so we take the negative of the negative value to get the original number). We add this value to our result. As we move the window to the right by one position, we add the new element into the heap and remove the elements from the heap that are no longer within the bounds of the current window. We repeat this process until we reach the end of the array.

### Code
```python
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = []    # Resultant list to store window max
        max_heap = []    # max heap

        # iterate through the first window
        for i in range(k):
            # store elements and their corresponding index
            # into the max heap
            heapq.heappush(max_heap, (-nums[i], i))
        
        # maximum element of the first window
        max_element = -max_heap[0][0]
        # add the maximum element of the first window
        window_max.append(max_element)

        # iterate through the rest of the windows
        for i in range(k, len(nums)):
            # remove the elements that are out of the current
            # window
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            # store the current element and its index into the heap
            heapq.heappush(max_heap, (-nums[i], i))
            # add the current maximum to the result
            window_max.append(-max_heap[0][0])
        
        return window_max
```

## Approach 2 $(TC: O(N), SC: O(K))$
A deque is initialized to store indices of array elements. The indices in the deque are always in decreasing order of their corresponding values in nums, ensuring the deque’s front always has the index of the maximum element for the current window. For the first k elements in nums, remove indices from the back of the deque if they point to elements smaller than the current element because they cannot be the maximum for the current or any subsequent windows; add the index of the current element to the back of the deque. For each new element in the array after the first window, remove indices from the front of the deque if they are out of the current window’s bounds (i.e., if they are smaller than the current index minus k); remove indices from the back of the deque if they point to elements smaller than the current element; add the index of the current element to the back of the deque; the front of the deque now holds the index of the maximum element for the current window, so add `nums[deque[0]]` to the result list. After sliding through all windows, the result list will contain the maximum value for each window position.

**Code for this approach is given in the python file**