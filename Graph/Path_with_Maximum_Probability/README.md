# Problem
You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i]` = `[a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

### Constraints
- 2 <= `n` <= 10<sup>4</sup>
- 0 <= `start`, `end` < n
- start != end
- 0 <= a, b < n
- a != b
- 0 <= `succProb.length` == `edges.length` <= 2 * 10<sup>4</sup>
- 0 <= `succProb[i]` <= 1
- There is at most one edge between every two nodes.

# Solution
## Approach $(TC: O(M \cdot \log N), SC: O(M + N))$
**M denotes the number of edges**

Since we have to find always find the path with the maximum probability for each node, we can use Djikstra's algorithm to solve this problem. In this approach, we initialized an adjacency list using the arrays `edges` and `succProb`. Then, we initialized an array `maxProb` to store the maximum probability found at each node while traversing the graph. Moreover, we make use of a max-heap to store the current probability and all the nodes to visit in the graph. We use max-heap to always find the path with the maximum probability and also in calculation to update the maximum probability for each node. 

At the start, we store the `start_node` into the max-heap along with its probability. Then we start traversing the vertices of the graph, checking if the `end_node` has been reached or not. If the `end_node` has been reached, we return the maximum probability. Otherwise, we travel along every edge of the node and update the maximum probability of all the vertices connecting the node on that edge. Then, we store the updated probability and the vertex into the max-heap. If we are unable to travel to the `end_node`, we return 0.

**Code for this approach is given in the python file**