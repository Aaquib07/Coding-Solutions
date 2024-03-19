# USING HEAP
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = []    # Resultant list to store window max
        max_heap = []    # max heap

        # iterate through the first window
        for i in range(k):
            # store elements and their corresponding index
            # into the max heap
            heapq.heappush(max_heap, (-nums[i], i))
        
        # maximum element of the first window
        max_element = -max_heap[0][0]
        # add the maximum element of the first window
        window_max.append(max_element)

        # iterate through the rest of the windows
        for i in range(k, len(nums)):
            # remove the elements that are out of the current
            # window
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            # store the current element and its index into the heap
            heapq.heappush(max_heap, (-nums[i], i))
            # add the current maximum to the result
            window_max.append(-max_heap[0][0])
        
        return window_max