# Problem
Given a non-negative integer `c`, decide whether there're two integers `a` and `b` such that a<sup>2</sup> + b<sup>2</sup> = c.

### Constraints
- 0 <= c <= 2<sup>31</sup> - 1

# Solution
## Approach 1 $(TC: O(\sqrt c \log c), SC: O(1))$
We can look at this question from a different perspective. Instead of finding both numbers a and b, we iterate over the possible values of a and for each value of a, we can easily find out b<sup>2</sup> (i.e., b<sup>2</sup> = c - a<sup>2</sup>). Then we just check whether the current b<sup>2</sup> is a perfect square or not. Now, we can see that the range of c is quite large, so we cannot perform a simple linear search. That is why, we need to perform binary search to find a number whose square equals b<sup>2</sup>.

### Code
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        def binary_search(left: int, right: int, n: int):
            # Iterate until left boundary exceeds right boundary
            while left <= right:
                # Calculate the mid value
                mid = (left + right) // 2
                # If the square of mid value equals n, then it is possible
                if mid ** 2 == n:
                    return True
                # If the square of mid value exceeds n
                elif mid ** 2 > n:
                    # Check the left half
                    right = mid - 1
                else:
                    # If the square of mid value is less than n
                    # check the right half
                    left = mid + 1
            # If the number cannot be found
            return False
                

        # 'a' can take values from 0 to sqrt(c)
        for a in range(int(c ** 0.5) + 1):
            # Square of b
            b_square = c - (a ** 2)
            # Check if the current b^2 value is perfect square
            possible = binary_search(0, b_square, b_square)
            # If it is, then return true
            if possible:
                return True
        
        # Otherwise, return false
        return False
```

## Approach 2 $(TC: O(\sqrt c), SC: O(1))$
We can further optimize the approach. We can eliminate the extra binary search operation using two pointers approach. We just initialize the left and right boundary number to 0 and $\sqrt c$ . Then we take the square of left boundary value as a<sup>2</sup> value and the square of right boundary value as b<sup>2</sup> value. If the sum equals to c, we return true. If the sum is smaller than c, we increment the left boundary value by 1. If the sum is greater than c, we decrement the right boundary value by 1. 

**Code for this approach is given in the python file**