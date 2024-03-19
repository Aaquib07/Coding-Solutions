# USING DE_QUEUE
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = []
        de_queue = deque()    # deque

        for i, num in enumerate(nums):
            # remove indices outside the current window
            while de_queue and de_queue[0] < i - k + 1:
                de_queue.popleft()
            
            # remove indices of all elements smaller than the
            # current element as they will not be needed for 
            # the max in the current window
            while de_queue and nums[de_queue[-1]] < nums[i]:
                de_queue.pop()
            
            # append the current number's index into the deque
            de_queue.append(i)

            # if the window has moved past the first k elements
            # then add to the result
            if i >= k - 1:
                window_max.append(nums[de_queue[0]])
        
        return window_max