from typing import List
from heapq import heappop, heappush

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def djikstra(graph: List[List[int]], src: int, dest: int) -> int:
            distances = [float('inf')] * len(graph)
            distances[src] = 0
            minHeap = [(0, src)]

            while minHeap:
                dist, node = heappop(minHeap)

                if dist > distances[node]:
                    continue

                for vertex, weight in graph[node]:
                    if dist + weight < distances[vertex]:
                        distances[vertex] = dist + weight
                        heappush(minHeap, (distances[vertex], vertex))
            
            return distances[dest]


        maxLimit = 2e9
        # Create the graph using edges
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))
        
        # Initial shortest distance
        currentShortestDistance = djikstra(graph, source, destination)
        if currentShortestDistance < target:
            return []
        
        if currentShortestDistance == target:
            # Update the edges having weight -1 to an impossible value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = maxLimit
            return edges
        
        # Adjust the edges
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            
            # Set the edge weight to 1 initially
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            # Compute the new shortest distance with updated edge weights
            newDistance = djikstra(graph, source, destination)

            if newDistance <= target:
                edges[i][2] += target - newDistance

                # Update the remaining edges with -1 weight to an impossible value
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = maxLimit
                return edges

        return []



if __name__ == '__main__':
    n = 5
    edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
    source = 0
    destination = 1
    target = 5
    result = Solution().modifiedGraphEdges(n, edges, source, destination, target)
    print(result)
