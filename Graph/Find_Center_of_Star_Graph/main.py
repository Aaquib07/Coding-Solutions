from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Extract nodes from the first edge
        u, v = edges[0][0], edges[0][1]
        other_edge = edges[1]

        # If any of the two nodes is present in the other edges, return it
        return u if u in other_edge else v



if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    result = Solution().findCenter(edges)
    print(result)
