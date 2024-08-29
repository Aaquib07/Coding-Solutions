from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(node: int):
            # Mark the stone as visited
            visited[node] = True

            # Iterate through every neighbor stones
            for neighbor in adjacencyList[node]:
                # If it is not visited
                if not visited[neighbor]:
                    # Perform a recursive DFS traversal
                    dfs(neighbor)


        n = len(stones)
        # Create an adjacency list
        adjacencyList = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                # Connect only those stones whose x-coordinates or y-coordinates match
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacencyList[i].append(j)
                    adjacencyList[j].append(i)

        # Stores whether a node has been seen before
        visited = [False] * n

        # Stores the number of connected components
        connectedComponents = 0
        # Iterate through every stone
        for i in range(n):
            # Perform a DFS traversal for every unvisited stone
            if not visited[i]:
                dfs(i)
                # Increment the number of connected components
                connectedComponents += 1
        
        # Stores the result
        result = n - connectedComponents
        return result


if __name__ == '__main__':
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    result = Solution().removeStones(stones)
    print(result)
