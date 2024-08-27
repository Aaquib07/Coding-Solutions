from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create an adjacency list graph
        graph = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            u, v = edge[0], edge[1]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        # Stores the maximum probability to reach nodes from start
        maxProb = [0.0] * n
        # Max-heap to store the nodes to visit along with the calculation of current probabilities for each node
        maxHeap = [(-1.0, start_node)]

        while maxHeap:
            currProb, node = heappop(maxHeap)

            # Return the probability if the end node is reached
            if node == end_node:
                return -currProb

            # Traverse through the connected vertices of the nodes and update the maximum probabilities for each of them
            for vertex, probability in graph[node]:
                if -currProb * probability > maxProb[vertex]:
                    maxProb[vertex] = -currProb * probability
                    heappush(maxHeap, (-maxProb[vertex], vertex))
        
        # If the end node cannot be reached
        return 0


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    result = Solution().maxProbability(n, edges, succProb, start, end)
    print(result)
