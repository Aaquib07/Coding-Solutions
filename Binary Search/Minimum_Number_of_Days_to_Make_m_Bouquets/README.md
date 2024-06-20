# Problem
You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

### Constraints
- bloomDay.length == n
- 1 <= n <= 10<sup>5</sup>
- 1 <= `bloomDay[i]` <= 10<sup>9</sup>
- 1 <= m <= 10<sup>6</sup>
- 1 <= k <= n

# Solution
## Approach $(TC: O(N \cdot \log(Max(bloomDay))), SC: O(1))$

At first, we check if the number of flowers are sufficient enough to make bouquets, returning -1 in that case indicating that it is impossible. Then we initialize left boundary to 0 and right boundary to maximum of the bloom days. We iterate until left boundary exceeds the right boundary. During the iteration, we initialize mid boundary and check for each of the bloom days whether the day is less than or equal to mid boundary value, incrementing the count of adjacent bloomed flowers in that case. Otherwise, we reset the count to 0 again. Then we check if the count becomes equal to k, if it is, then we increment the count of bouquets. Lastly, we check if the bouquets are sufficient or not; if it is sufficient, then we update the result to the mid boundary value and update the right boundary to search in the left half. Otherwise, we update the left pointer to search in the right half.

**Code for this approach is given in the python file**