# Problem
Given an array of `points` where points[i] = [x~i~, y~i~] represents a point on the X-Y plane and an integer `k`, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2^ + (y1 - y2)^2^).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### Constraints
- 1 <= k <= points.length <= 10^4^
- -10^4^ <= x~i~, y~i~ <= 10^4^

# Solution
## Approach (TC: O(N * log K), SC: O(K))
We start by initializing a max-heap. We iterate through every point and calculate the negative of the distance from origin (**REASON:** Python's built-in heapq module implements a min-heap that's why negative distance). We add the negative distance, x-coordinate and y-coordinate of the point into the max-heap. Then we check if the length of the max-heap exceeds `k`, we pop the largest distance point from the max-heap. Lastly, our heap contains all the required k closest points so we add them into our result.

**Code for this approach is given in the python file**