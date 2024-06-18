# Problem
You are given an array of integers `stones` where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

If `x == y`, both stones are destroyed, and
If `x != y`, the stone of weight x is destroyed, and the stone of weight `y` has new weight `y - x`.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

### Constraints
- 1 <= stones.length <= 30
- 1 <= `stones[i]` <= 1000

# Solution
## Approach $(TC: O(N \cdot log N), SC: O(N))$
We start by initializing a max-heap. We iterate through every stone weight and add the negative of the stone weight into the max-heap (**REASON:** Python's built-in heapq module implements a min-heap that's why negative distance). While there are elements in the max-heap, we pop two greatest stone weight from the heap (x and y). If the weight differs, we just update the weight of the heavier stone and push the updates stone back to the heap. While iterating, we check if the length of heap is 0, we return 0. If the length of heap is 1, we just return the weight of the stone left.

**Code for this approach is given in the python file**