from typing import List
from heapq import heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []    # Stores the k closest points from origin
        max_heap = []    # Max-heap

        # Calculate the negative distance of all the points from origin
        for x, y in points:
            distance_from_origin = -((x ** 2) + (y ** 2))
            # Add the negative distance, x-coordinate, y-coordinate into the heap
            heappush(max_heap, (distance_from_origin, x, y))

            # If the length of max-heap exceeds k
            if len(max_heap) > k:
                # Pop the largest element from the heap
                heappop(max_heap)
        
        # Store the remaining k closest points to our result
        for distance, x, y in max_heap:
            result.append([x, y])
        
        return result
        

if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = Solution().kClosest(points, k)
    print(result)