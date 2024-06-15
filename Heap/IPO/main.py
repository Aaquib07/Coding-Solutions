from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # Initialize projects list consisting of tuples (capital[i], profits[i])
        projects = [(ci, pi) for ci, pi in zip(capital, profits)]
        # Sort the projects according to capital
        projects.sort()

        max_heap = []    # Max-heap to store profits
        index = 0

        for _ in range(k):
            # Until the capital is less or equal to w
            while index < n and projects[index][0] <= w:
                # Push the profit to the max-heap
                heappush(max_heap, -projects[index][1])
                # Increment the index
                index += 1

            # If there are elements in the max-heap
            if max_heap:
                # Add the profit to w
                w -= heappop(max_heap)

        return w



if __name__ == '__main__':
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    result = Solution().findMaximizedCapital(k, w, profits, capital)
    print(result)
