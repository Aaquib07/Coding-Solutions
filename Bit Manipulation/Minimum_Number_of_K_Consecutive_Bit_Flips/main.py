from typing import List
from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Keeps track of flips
        queue = deque()
        # Current flip state
        flip_state = 0
        # Stores the minimum flips
        result = 0

        for index, element in enumerate(nums):
            # Remove the flip that is out of the current window
            if index >= k:
                flip_state ^= queue[0]
            
            # If the current bit is 0
            if flip_state == nums[index]:

                # If the subarray starting from the current index cannot be flipped
                if index + k > n:
                    return -1

                # Add a flip at this index
                queue.append(1)
                # Toggle the flip state
                flip_state ^= 1
                # Increment the result
                result += 1
            else:
                queue.append(0)
            
            # Remove the oldest bit if the size of queue exceeds k
            if len(queue) > k:
                queue.popleft()
        
        return result



if __name__ == '__main__':
    nums = [0, 1, 0]
    k = 1
    result = Solution().minKBitFlips(nums, k)
    print(result)
