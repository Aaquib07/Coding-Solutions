# Problem
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between x~start~ and x~end~. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if x~start~ <= x <= x~end~. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

### Constraints
- 1 <= points.length <= 10^5^
- points[i].length == 2
- -2^31^ <= x~start~ < x~end~ <= 2^31^ - 1

# Solution
## Approach (TC: O(N log(N)), SC: O(1))
At first we sort the points according to x~start~. We sort the points so that we can get the required number of arrows in a single iteration. Now, we initialize the required arrows to 1 as because we require atleast 1 arrow to burst all the balloons (when all the balloons will be on the same vertical line, we need only 1 arrow). We start iterating the points array and check whether x~start~ of the current balloon lies ahead of the minimum x~end~ of the previous balloons. If the condition satisfies, we increment the number of arrows to be used and update the x~end~. Otherwise, we just greedily take the minimum of the current x~end~ of the balloon and the previous minimum x~end~ of the balloon.