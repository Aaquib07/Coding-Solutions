# Problem
You are given two integer arrays `energyDrinkA` and `energyDrinkB` of the same length `n` by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.

You want to maximize your total energy boost by drinking one energy drink per hour. However, if you want to switch from consuming one energy drink to the other, you need to wait for one hour to cleanse your system (meaning you won't get any energy boost in that hour).

Return the maximum total energy boost you can gain in the next `n` hours.

**Note:** You can start consuming either of the two energy drinks

### Constraints
- n == `energyDrinkA.length` == `energyDrinkB.length`
- 3 <= `n` <= 10<sup>5</sup>
- 1 <= `energyDrinkA[i]`, `energyDrinkB[i]` <= 10<sup>5</sup>

# Solution
## Approach 1 $(TC: O(2^N), SC: O(Recursion Stack Space))$
In this approach, we take the help of recursion to solve the problem. We define a function `recursion(index: int, drinkATaken: bool)` in which `index` signifies the current index and `drinkATaken` signifies whether drinkA has been taken currently or not. The base case is when the index goes out of bound (we return 0 in that case because no energy can be gained further). Then we check if drink A is taken or not. If it is taken, then we add `energyDrinkA[index]` and recursively take the maximum of two scenarios: 

1. Take the energy from drink A at `index + 1`
2. Take the energy from drink B at `index + 2`

Similarly, if the drink A is not taken, then we add `energyDrinkB[index]` and recursively take the maximum of two scenarios:

1. Take the energy from drink B at `index + 1`
2. Take the energy from drink A at `index + 2`

Then, we return the maximum out of the above two possible situations (i.e., when drink A is taken and when drink A is not taken)

Lastly, we call the recursive function starting with index 0 twice - because we can start either with drink A or drink B. Then we return the maximum of them.

### Code
```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        def recursion(index: int, drinkATaken: bool) -> int:
            # Base case: If index goes out of bound
            if index >= n:
                return 0
            
            take, notTake = 0, 0
            if drinkATaken:
                # Add the energy from drink A along with the max between energy at index + 1 of drink A and energy at index + 2 of drink B
                take = energyDrinkA[index] + max(recursion(index + 1, True), recursion(index + 2, False))
            else:
                # Add the energy from drink B along with the max between energy at index + 1 of drink B and energy at index + 2 of drink A
                notTake = energyDrinkB[index] + max(recursion(index + 1, False), recursion(index + 2, True))
            
            return max(take, notTake)


        n = len(energyDrinkA)
        # Take the maximum out of the two possibilties: when drinkA is taken first and when drink B is taken first
        return max(recursion(0, True), recursion(0, False))
```

## Approach 2 $(TC: O(N), SC: O(N + Recursion Stack Space)$
We can optimize the above recursive solution using memoization. This is because the problem involves overlapping subproblems. In this approach, we initialize a 2d array `memo` of dimension N x 2. We store the computed value at each index to our `memo` so that repetitive computation does not take place. The remaining process remains the same.

### Code
```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        def topdown(index: int, drinkATaken: bool) -> int:
            # Base case: If index goes out of bound
            if index >= n:
                return 0
            
            # If the result has already been computed, return it
            if memo[index][drinkATaken] != -1:
                return memo[index][drinkATaken]

            take, notTake = 0, 0
            if drinkATaken:
                # Add the energy from drink A along with the max between energy at index + 1 of drink A and energy at index + 2 of drink B
                take = energyDrinkA[index] + max(topdown(index + 1, True), topdown(index + 2, False))
            else:
                # Add the energy from drink B along with the max between energy at index + 1 of drink B and energy at index + 2 of drink A
                notTake = energyDrinkB[index] + max(topdown(index + 1, False), topdown(index + 2, True))
            
            # Store the maximum of both situations into the memo
            memo[index][drinkATaken] = max(take, notTake)
            return memo[index][drinkATaken]


        n = len(energyDrinkA)
        memo = [[-1] * 2 for _ in range(n + 1)]
        # Take the maximum out of the two possibilties: when drinkA is taken first and when drink B is taken first
        return max(topdown(0, True), topdown(0, False))
```

## Approach 3 $(TC: O(N), SC: O(N))$
Now to avoid the extra stack space in the previous approach, we use tabulation technique. In this approach, we initialize a 2-d array `dp` of dimension (N + 1) $\times$ 2. Since it is a bottom up approach, we start from index `n` and finish at index 0. 

At first, we initialize the entries at index `n` to 0 for the base case scenario (i.e., when index goes out of bound). Then we iterate from the index `n - 1` till 0 and for each index we take two possibilties: whether the drink A is taken or not. If the drink A is taken, we add the energy of drink A at that index along with the maximum of `dp[index + 1][1]` and `dp[index + 2][0]`. If the drink A is not taken, we add the energy of drink B at that index along with the maximum of 'dp[index + 1][0]' and `dp[index + 2][1]`. Then we store the result into our dp array. Lastly we return the maximum out of two scenarios: whether drink A or drink B is taken first.

### Code
```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # Initialize dp array
        dp = [[-1] * 2 for _ in range(n + 1)]

        # Base case: when index goes out of bound
        dp[n][0] = 0
        dp[n][1] = 0

        for index in range(n - 1, -1, -1):
            for drinkATaken in range(2):
                take, notTake = 0, 0
                # If drink A is taken
                if drinkATaken:
                    # Check whether index + 2 goes out of bound
                    if index + 2 <= n:
                        take = energyDrinkA[index] + max(dp[index + 1][1], dp[index + 2][0])
                    else:
                        take = energyDrinkA[index] + max(0, dp[index + 1][1])
                # If drink is not taken
                else:
                    # Check whether index + 2 goes out of bound
                    if index + 2 <= n:
                        notTake = energyDrinkB[index] + max(dp[index + 1][0], dp[index + 2][1])
                    else:
                        notTake = energyDrinkB[index] + max(0, dp[index + 1][0])
                
                # Store the maximum of both situations
                dp[index][drinkATaken] = max(take, notTake)
        
        # Return the maximum of both scenarios: when drink A is taken first and when drink B is taken first
        return max(dp[0])
```

## Approach 4 $(TC: O(N), SC: O(1))$
If we observe carefully the previous approach, we can see that only the consecutive three rows of `dp` array (`dp[index]`, `dp[index + 1]`, `dp[index + 2]`) are involved in the process. So, instead of initializing a full dp array, we just initialize the three rows separately (`curr`, `prev`, `prevOfPrev`) containing only 2 entries. At the start, we treat `prevOfPrev` as the last row of dp. So, we compute the base case scenario on it. The iteration process is similar to the previous approach. The only difference is that after the computation of all the entries of current row, we assign the entries of `prev` to `prevOfPrev` and `curr` to `prev`.

**Code for this approach is given in the python file**