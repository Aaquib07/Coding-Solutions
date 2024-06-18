# Problem
Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

### Constraints
- 1 <= nums.length <= 1000
- 1 <= `nums[i]` <= 10<sup>4</sup>
- `nums` is sorted in ascending order.
- 1 <= n <= 2<sup>31</sup> - 1

# Solution
## Approach $(TC: O(N), SC: O(1))$
At first, we initialize a variable named `missing_sum` to 1 that indicates the sum missing from the `nums` list. Then we start iterating until we reach a missing sum greater than n. At each iteration, we greedily check if the number at the current index is less or equal to the missing sum; adding the number in that case. This is because we can include the number to achieve that missing sum. On the other hand, it the number at the current index is greater than the missing sum, then we add/patch a number equal to the difference between the missing sum and the current number and also increment the count of additional number. Lastly we return the result.

**Code for this approach is given in the python file**