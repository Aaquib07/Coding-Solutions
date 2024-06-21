# Problem
There is a bookstore owner that has a store open for `n` minutes. Every minute, some number of customers enter the store. You are given an integer array `customers` of length n where `customers[i]` is the number of the customer that enters the store at the start of the i<sup>th</sup> minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array `grumpy` where `grumpy[i]` is 1 if the bookstore owner is grumpy during the i<sup>th</sup> minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for `minutes` consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

### Constraints
- n == customers.length == grumpy.length
- 1 <= minutes <= n <= 2 * 10<sup>4</sup>
- 0 <= `customers[i]` <= 1000
- `grumpy[i]` is either 0 or 1.

# Solution

## Approach $(TC: O(N), SC: O(1))$

We start with a window of length `minutes` and just add the customers in the window as because the owner is not grumpy in these special minutes. For the rest of the window, we only add those customers in which the owner is not grumpy. These are the result for the current window. Now we shift the window by removing the customers from the previous window one by one and adding the customers from the current window one by one. Then we repetitively update the result.

**Code for this approach is given in the python file**