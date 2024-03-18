# Problem
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

### Constraints
- 1 <= nums.length <= 10^4^
- 0 <= nums[i] <= 10^5^

# Solution
## Approach (TC: O(N), SC: O(1))
We can see the problem at hand from a different perspective. We initially set the target position to be the last index of the array. Then we start iterating from the second last index and find whether we can reach the last index from there by maximum jump. We can find the resultant index that we will be reaching at by calculating `i + nums[i]` as this indicates at what maximum index we can go by taking a maximum jump of nums[i] from the current index i. If we are able to reach the last index or beyond last index, we update the target position to be the second last index. Now our target is to reach the second last index. This process repeats until we get to the starting index 0. Now if last updated target position is 0, that means we can reach the last index from index 0 and we return true otherwise, we return false.