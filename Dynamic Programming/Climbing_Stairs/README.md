# Problem
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Constraints
- 1 <= n <= 45

# Solution
## Approach 1 $(TC: O(2^N), SC: O(Recursion Stack Space))$
Our first brute force approach is recursion. We aim to start the recursion from the n^th^ step to the 0^th^ step. The base case is when we need to climb 0 stair and 1 stair. There's only 1 way in which we can climb no stairs or 1 stair. The we recursively calculate the number of ways to climb  from the (i - 1)^th^ and (i - 2)^th^ steps and add them. Lastly we return the total number of ways.

### Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive function to calculate the number of ways to climb n stairs
        def recursion(idx):
            # Base cases: There is 1 way to climb 0 or 1 stair
            if idx <= 1:
                return 1
            
            # Calculate the number of ways to climb idx stairs recursively
            ways = recursion(idx - 1) + recursion(idx - 2)
            return ways
        
        # Call the recursive function with the initial index (n) and return the result
        return recursion(n)
```

## Approach 2 $(TC: O(N), SC: O(N) + O(Recursion Stack Space))$
Our second approach is memoization. We are able to memoize the recursive solution because there are overlapping subproblems. We can cache the results so that we can avoid re-computing them in the future. Since only 1 parameter is varying in this problem - index, cache array (or dp array) needs to be 1 dimensional and it keeps track of the values computed at each index. Here the only difference that exists from the recursive solution is that we store the values that we get from recursion and just make an additional check if the calculation for the current index has been done already or not, returning the value if done already.

### Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive function using top-down dynamic programming
        def topDown(idx, dp):
            # Base cases: There is 1 way to climb 0 or 1 stair
            if idx <= 1:
                return 1
            
            # Check if the result for idx is already calculated and stored in dp
            if dp[idx] != -1:
                return dp[idx]
            
            # Calculate the number of ways to climb idx stairs recursively
            ways = topDown(idx - 1, dp) + topDown(idx - 2, dp)
            # Store the result in dp to avoid redundant calculations
            dp[idx] = ways
            return dp[idx]

        # Initialize a dp array to store intermediate results for each number of stairs
        dp = [-1 for _ in range(n + 1)]
        # Call the recursive function with the initial index (n) and dp array
        return topDown(n, dp)
```

## Approach 3 $(TC: O(N), SC: O(N))$
Since memoization takes an extra space consisting of the recursion stack space, we can optimize the approach to avoid using that additional space through tabulation. In thiss approach, we just start from the base case i.e., index 0 and go through index n in the opposite manner. The only difference between this approach and previous approach is that we just reverse the iteration manner (start from base case) to avoid the use of recursion. At index 0 and 1 of dp array, we store 1 as because the number of ways to climb 0 stairs and 1 stair is 1. We iterate and make use of the (i - 1)^th^ index and (i - 2)^th^ index to calculate the number of ways for the i^th^ index.

### Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize a DP (dynamic programming) array to store intermediate results
        dp = [-1 for _ in range(n + 1)]
        
        # Base cases: There is 1 way to climb 0 or 1 stair
        dp[0] = 1
        dp[1] = 1

        # Fill in the DP array with the number of ways to climb each number of stairs
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the result for climbing n stairs (stored at index n in the DP array)
        return dp[n]
```

## Approach 4 $(TC: O(N), SC: O(1))$
Now there is one thing to notice. In all of the above approaches, if we are currently calculating the number of ways at index i, we just require the (i - 1)^th^ index value and (i - 2)^th^ index value. So, there's a chance of optimizing the space complexity. For the value at (i - 2)^th^ index, we initialize a variable `prev_of_prev` and for the value at (i - 2)^th^ index, we initialize a variable `prev`. Then we perform iteration in the same way as that in the case of tabulation and just keep updating `prev` and `prev_of_prev` when calculating the current index value.

**Code for this approach is given in the python file**