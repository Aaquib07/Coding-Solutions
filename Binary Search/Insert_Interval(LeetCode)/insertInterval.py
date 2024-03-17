from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if the intervals list is empty, then we return 
        # only the newInterval
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # binary search to find the correct index to insert newInterval
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Insert newInterval at the found index
        intervals.insert(left, newInterval)

        result = []
        for interval in intervals:
            # if the result is empty or there is no overlap
            # then we add the interval as it is
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            # if there is an overlap, then we merge the intervals
            # by updating the end time of the last interval in result
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result


if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    result = Solution().insert(intervals, newInterval)
    print(result)