from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # If there is only one stone initially
        if len(stones) == 1:
            # Return its weight
            return stones[0]
        
        max_heap = []    # Max-heap
        # Add the stone weights into the heap
        for weight in stones:
            max_heap.append(-weight)
        
        # Heapify
        heapify(max_heap)
        
        while max_heap:
            y = -heappop(max_heap)    # Heaviest stone
            x = -heappop(max_heap)    # Second heaviest stone
            
            # If the weight of the second heaviest stone is smaller
            # than that of the heaviest stone
            if x < y:
                # Update the weight of heaviest stone
                y -= x
                # Add the updated stone into the heap
                heappush(max_heap, -y)
            
            # If there is no stones left
            if not max_heap:
                return 0
            
            # If there is a single stone left
            if len(max_heap) == 1:
                # Return its weight
                return -max_heap[0]



if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    result = Solution().lastStoneWeight(stones)
    print(result)