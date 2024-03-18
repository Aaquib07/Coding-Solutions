from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the target position as the last index
        goal_position = len(nums) - 1

        # iterate from the back of the array
        for index in range(len(nums) - 2, -1, -1):
            # maximum position we can go ahead from the
            # current index
            max_position_from_index = index + nums[index]
            # if we are able to reach the target position
            # from the current index
            if max_position_from_index >= goal_position:
                # we set the current index as the new 
                # target position
                goal_position = index
        
        # if we are able to reach last index from index 0
        if goal_position == 0:
            # we return true
            return True
        
        # otherwise, we return False
        return False