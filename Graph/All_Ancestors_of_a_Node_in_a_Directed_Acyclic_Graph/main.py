from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(node: int, visited: set):
            # Mark the current node
            visited.add(node)

            # Recursively traverse all its neighbor nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)


        # Initialize graph as an adjacency list
        graph = [[] for _ in range(n)]

        # Populate the graph with reversed edges
        for u, v in edges:
            graph[v].append(u)
        
        # Ancestors list
        result = []

        # For each node, find all its ancestors
        for i in range(n):
            ancestors = []
            visited = set()
            dfs(i, visited)

            # Add visited nodes to the ancestor list of current node
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)

            result.append(ancestors)

        return result


if __name__ == '__main__':
    n = 8
    edgeList = [[0, 3], [0, 4], [1, 3],[2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    result = Solution().getAncestors(n, edges=edgeList)
    print(result)
