# Problem
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given `n` projects where the ith project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most `k` distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

### Constraints
- 1 <= k <= 10<sup>5</sup>
- 0 <= w <= 10<sup>9</sup>
- n == `profits.length`
- n == `capital.length`
- 1 <= n <= 15<sup>5</sup>
- 0 <= `profits[i]` <= 10<sup>4</sup>
- 0 <= `capital[i]` <= 10<sup>9</sup>

# Solution
## Approach $(TC: O(N \cdot \log N + K \cdot logN), SC: O(N))$
Through the question we can observe that we always need the smallest capital so that we can afford to start the project. Therefore, we start by storing the capital needed and profit gained by the projects in a list. Then we sort the list according to the capital in ascending order. 

```python
projects = [(ci, pi) for ci, pi in zip(capital, profits)]
projects.sort()
```

To store the profits, we initialize a max-heap as because we always need the maximum possible profit. Then we start iterating until we pick k projects. We run another loop and check whether the current capital is less than or equal to `w` (Condition to afford the project). If it is the case, then we add the corresponding profit into the max-heap. After the iteration is over, we just add the profits to `w`. Lastly, we return it. 

```python
max_heap = []    # Max-heap to store profits
index = 0

for _ in range(k):
    # Until the capital is less or equal to w
    while index < n and projects[index][0] <= w:
        # Push the profit to the max-heap
        heappush(max_heap, -projects[index][1])
        # Increment the index
        index += 1

    # If there are elements in the max-heap
    if max_heap:
        # Add the profit to w
        w -= heappop(max_heap)

return w
```

**Code for this approach is given in the python file**