# Problem
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.

### Constraints
- 1 <= nums.length <= 10^5^
- 1 <= nums[i] <= 10^6^
- 1 <= k <= 10^5^

# Solution
## Approach (TC: O(N), SC: O(N))
We first calculate the maximum element of the list `nums`. We intialize a variable `max_element_count_in_window` to keep track of the count of maximum element in the sliding window. Then we intialize a left pointer (`left`) to point at index 0 and start iterating through `nums` using right pointer (`right`). While expanding the window, we check if the element at the right pointer is the maximum element, we increment  `max_element_count_in_window` by 1. If the count of maximum element in the window becomes k, we shrink the window until the count of maximum element in the window becomes less than `k`. While shrinking the window, if the element at the left pointer is the maximum element, we decrement the count of maximum element in the window and increment the left pointer. In this way, the left pointer actually keeps track of all the possible start positions of the valid subarrays. We just add the count of those positions to our result. Lastly we return the result 

**Code for this approach is given in the python file**