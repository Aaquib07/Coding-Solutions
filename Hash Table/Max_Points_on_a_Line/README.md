# Problem
Given an array of points where points[i] = [x<sub>i</sub>, y<sub>i</sub>] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

### Constraints
- 1 <= points.length <= 300
- points[i].length == 2
- -10<sup>4</sup> <= x<sub>i</sub> , y<sub>i</sub> <= 10<sup>4</sup>
- All the points are unique.

# Solution
## Approach (TC: O(N<sup>2</sup>), SC: O(N))
We start with iterating through all the points. For each and every point, we initialize a hashmap to store the count of slope made by these points. We also initialize variable named `same_points` to store the number of same points. Then we just iterate through all the remaining points and calculate the slope made by these points. Then we store the count of the slope in the hashmap. Lastly, we just add the number of same points to the max count of a slope. 

**Code for this approach is given in the python file**