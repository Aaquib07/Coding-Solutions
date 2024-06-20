from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Stores the total profit
        result = 0
        # Stores the maximum ability
        max_ability = max(worker)
        # Stores the profit for each ability from 0 to max_ability
        jobs = [0] * (max_ability + 1)

        # Iterate through all the difficulty levels
        for i in range(len(difficulty)):
            # If the difficulty level is less than or equal to
            # the maximum ability of all the workers
            if difficulty[i] <= max_ability:
                # Update the corresponding level index as the maximum of
                # current profit and the previous profit
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])

        # Store the running max of all the profits
        for i in range(1, max_ability + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        
        # Add the profit corresponding to the ability of workers into the result
        for ability in worker:
            result += jobs[ability]
        
        return result


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    result = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(result)
