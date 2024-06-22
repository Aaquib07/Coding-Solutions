# Problem
Given an array of integers `nums` and an integer `k`. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

### Constraints
- 1 <= nums.length <= 50000
- 1 <= `nums[i]` <= 10<sup>5</sup>
- 1 <= k <= nums.length


# Solution
## Approach 1 $(TC: O(N), SC: O(1))$
At first, we define a function that counts the number of subarrays having at most `x` odd numbers. In that function, we initialize a variable `count` to store the count of odd numbers in the array. We intialize a left pointer to point at the starting index and then iterate over the aray using right pointer and check if the number at the right pointer index is odd, then we increment the count. If the count exceeds `x`, then we shrink the window from the left side. We check if the number at the left pointer index is odd, then we decrement the count; then we increment the left pointer. Once we get the desired subarray window, we update the result. Then we call the function two times, once with `k` and once with `k - 1`. Then we subtract the result of function with `k - 1` as parameter from the result of function with k as parameter. 

**Code for this approach is given in the python file**