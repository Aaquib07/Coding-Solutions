# Problem
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

### Constraints
- 1 <= nums.length <= 3 * 10<sup>4</sup>
- 1 <= `nums[i]` <= 1000
- 0 <= k <= 10<sup>6</sup>

# Solution
## Approach $(TC: O(N), SC: O(1))$
We initialize a variable named `product` to store the product of the subarrays. Then we use sliding window technique using two pointers to find all the valid subarrays. We initialize left pointer to point at 0<sup>th</sup> index and then iterate through the list using right window (expand the window using right pointer and shrink the window using left pointer). We iteratively add the element at the right pointer to our product. If the product becomes greater than or equal to k, we shrink the window from the left side until it again becomes less than k. Then we update the total count of valid subarrays. Lastly we return the total count.

**Code for this approach is given in the python file**