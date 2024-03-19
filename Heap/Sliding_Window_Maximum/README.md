# Problem
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

### Constraints
- 1 <= nums.length <= 10^5^
- -10^4^ <= nums[i] <= 10^4^
- 1 <= k <= nums.length

# Solution
## Approach 1 (TC: O(N log(K)), SC: O(K))
We start by creating a max heap that will store pairs of values from the array nums. Each pair consists of the negative value of an element (since Python’s heapq is a min-heap, we use negative values to simulate a max heap) and its index in the array. We fill the heap with the first k elements from the array. This represents the first window. The root of the heap contains the maximum value of the first window (remember, it’s stored as a negative number, so we take the negative of the negative value to get the original number). We add this value to our result. As we move the window to the right by one position, we add the new element into the heap and remove the elements from the heap that are no longer within the bounds of the current window. We repeat this process until we reach the end of the array.

## Approach 2 (TC: O(N), SC: O(K))
A deque is initialized to store indices of array elements. The indices in the deque are always in decreasing order of their corresponding values in nums, ensuring the deque’s front always has the index of the maximum element for the current window. For the first k elements in nums, remove indices from the back of the deque if they point to elements smaller than the current element because they cannot be the maximum for the current or any subsequent windows; add the index of the current element to the back of the deque. For each new element in the array after the first window, remove indices from the front of the deque if they are out of the current window’s bounds (i.e., if they are smaller than the current index minus k); remove indices from the back of the deque if they point to elements smaller than the current element; add the index of the current element to the back of the deque; the front of the deque now holds the index of the maximum element for the current window, so add nums[deque[0]] to the result list. After sliding through all windows, the result list will contain the maximum value for each window position.