from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # N-th row of dp
        prevOfPrev = [-1] * 2

        # Base case: when index goes out of bound
        prevOfPrev[0] = 0
        prevOfPrev[1] = 0
        
        # N - 1 th row of dp
        prev = [-1] * 2

        for index in range(n - 1, -1, -1):
            # Current row
            curr = [-1] * 2
            for drinkATaken in range(2):
                take, notTake = 0, 0
                # If drink A is taken
                if drinkATaken:
                    # Check whether index + 2 goes out of bound
                    if index + 2 <= n:
                        take = energyDrinkA[index] + max(prev[1], prevOfPrev[0])
                    else:
                        take = energyDrinkA[index] + max(0, prev[1])
                # If drink is not taken
                else:
                    # Check whether index + 2 goes out of bound
                    if index + 2 <= n:
                        notTake = energyDrinkB[index] + max(prev[0], prevOfPrev[1])
                    else:
                        notTake = energyDrinkB[index] + max(0, prev[0])

                # Update the current row entries
                curr[drinkATaken] = max(take, notTake)
            
            # Assign the second last row entries to the last row
            prevOfPrev = prev
            # Assign the current row entries to the second last row
            prev = curr
        
        # Return the maximum of both scenarios: when drink A is taken first and when drink B is taken first
        return max(prev)


if __name__ == '__main__':
    energyDrinkA = [4, 1, 3, 5, 2, 1]
    energyDrinkB = [1, 1, 5, 2, 1, 5]
    result = Solution().maxEnergyBoost(energyDrinkA, energyDrinkB)
    print(result)