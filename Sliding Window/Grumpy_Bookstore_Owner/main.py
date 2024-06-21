from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Length of customers list
        n = len(customers)
        # Stores the number of satisfied customers
        satisfied = 0

        # Iterate through first secret technique minutes
        for i in range(minutes):
            # Add the customers
            satisfied += customers[i]

        # Iterate from the ending of secret technique minute to end of array
        for i in range(minutes, n):
            # Add the customers in which owner is not grumpy
            satisfied += (1 - grumpy[i]) * customers[i]

        # Stores the maximum satisfied customers
        result = satisfied

        # Iterate from the ending of secret technique minute to end of array 
        for i in range(minutes, n):
            # Remove the customers from the pervious window
            satisfied -= grumpy[i - minutes] * customers[i - minutes]
            # Add the customers in the current window
            satisfied += grumpy[i] * customers[i]
            # Update the result
            result = max(result, satisfied)
        
        return result

        



if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    result = Solution().maxSatisfied(customers, grumpy, minutes)
    print(result)
