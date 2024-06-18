# Problem
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

### Constraints
- 1 <= nums.length <= 10<sup>5</sup>
- nums[i] is either 0 or 1.

# Solution
## Approach $(TC: O(N), SC: O(N))$
We use a hashmap to store the current sum and the index where it appears. Initially we set the current sum to 0 and index to -1. We initialize curr_sum (it keeps track of the current sum) with 0. We initialize another variable called max_length with 0. Now, we iterate over the array and if the current element is 1, we increment the sum otherwise we decrement it. If the current sum is not there in the hashmap, we just add it along with the index. But if the current sum already exists in the hashmap, we calculate the length of the new subarray as the difference between the current index and previous index at which it appears. Then we update the max_length accordingly. Lastly we return thee max_length.