# Problem
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where `points[i]` = [x<sub>start</sub>, x<sub>end</sub>] denotes a balloon whose horizontal diameter stretches between x<sub>start</sub> and x<sub>end</sub> . You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if x<sub>start</sub> <= x <= x<sub>end</sub> . There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

### Constraints
- 1 <= points.length <= 10<sup>5</sup>
- points[i].length == 2
- -2<sup>31</sup> <= x<sub>start</sub> < x<sub>end</sub> <= 2<sup>31</sup> - 1

# Solution
## Approach $(TC: O(N log(N)), SC: O(1))$
At first we sort the points according to x<sub>start</sub>. We sort the points so that we can get the required number of arrows in a single iteration. Now, we initialize the required arrows to 1 as because we require atleast 1 arrow to burst all the balloons (when all the balloons will be on the same vertical line, we need only 1 arrow). We start iterating the points array and check whether x<sub>start</sub> of the current balloon lies ahead of the minimum x<sub>end</sub> of the previous balloons. If the condition satisfies, we increment the number of arrows to be used and update the x<sub>end</sub>. Otherwise, we just greedily take the minimum of the current x<sub>end</sub> of the balloon and the previous minimum x<sub>end</sub> of the balloon.

**Code for this approach is given in the python file**