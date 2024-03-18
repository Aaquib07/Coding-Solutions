from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the points array based on the starting x
        # coordinate
        points.sort()
        # initialize the required number of arrows as 1
        # because it's the most minimum we can have
        # when all balloons will be in the same vertical line
        result = 1
        # ending x coordinate 
        end_x_prev = points[0][1]

        for i in range(1, len(points)):
            start_x = points[i][0]
            # if the starting x coordinate of the i-th
            # balloon is larger than previous end x
            # coordinate
            if start_x > end_x_prev:
                # we increment the number of required arrows
                result += 1
                # we update the ending x coordinate
                end_x_prev = points[i][1]
            else:
                # otherwise, we update the ending x coordinate
                # as the minimum of the current ending x coordinate
                # and the previous ending x coordinate
                end_x_prev = min(end_x_prev, points[i][1])
        
        return result