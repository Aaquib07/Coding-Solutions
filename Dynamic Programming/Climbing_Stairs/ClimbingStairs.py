class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables to store the number of ways for climbing 0 and 1 stair
        prev_of_prev = 1  # Number of ways to climb 0 stair
        prev = 1  # Number of ways to climb 1 stair

        # Iterate from 2 to n (inclusive) to calculate the number of ways to climb each number of stairs
        for i in range(2, n + 1):
            # Calculate the number of ways to climb i stairs by adding the ways to climb i-1 and i-2 stairs
            current = prev + prev_of_prev
            # Update prev_of_prev and prev for the next iteration
            prev_of_prev = prev
            prev = current
        
        # Return the number of ways to climb n stairs, which is stored in prev
        return prev


if __name__ == '__main__':
    n = 4
    result = Solution().climbStairs(n)
    print(result)  
