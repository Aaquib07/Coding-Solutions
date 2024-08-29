# Problem
You are given an array of non-overlapping intervals `intervals` where `intervals[i]` = [start<sub>i</sub> , end<sub>i</sub>] represent the start and the end of the i<sup>th</sup> interval and intervals is sorted in ascending order by start<sub>i</sub> . You are also given an interval `newInterval` = [start, end] that represents the start and end of another interval.

Insert `newInterval` into intervals such that intervals is still sorted in ascending order by start<sub>i</sub> and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
**Note** that you don't need to modify intervals in-place. You can make a new array and return it.

### Constraints
- 0 <= `intervals.length` <= 10<sub>4</sub>
- `intervals[i].length` == 2
- 0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>5</sup>
- intervals is sorted by start<sub>i</sub> in ascending order.
- `newInterval.length` == 2
- 0 <= start <= end <= 10<sup>5</sup>

# Solution
## Approach 1 $(TC: O(N), SC: O(N))$
The first approach is to compare the newInterval with all the intervals one by one. We compare the ending time of the interval at index i with the start time of the newInterval. If the ending time of the i<sup>th</sup> index interval is less than the starting time of the newInterval, then we can add the i<sup>th</sup> index interval in our result (as there is no overlap) and increment the index. But if the ending time of the newInterval is greater than the starting time of the interval at index i, then we can have several cases:

1. Starting time of the newInterval may be less than that of i<sup>th</sup> index interval
2. Starting time of the i<sup>th</sup> index interval may be less than that of the newInterval
3. Ending time of the newInterval may be greater than that of i<sup>th</sup> index interval
4. Ending time of the i<sup>th</sup> index interval may be greater than that of the newInterval

For case 1 and 2, we can take the minimum of them and initialize new start time with that value. For case 3 and 4, we can take the maximum of them and initializee new end time with that value. Then we add the resulting interval into our result. Lastly, we add rest of the intervals.

### Code
```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        index = 0
        result = []

        # No overlapping before merging intervals
        while index < n and intervals[index][1] < newInterval[0]:
            # Add the old interval if the ending time of old
            # interval is before the starting time of newInterval
            result.append(intervals[index])
            # Increment the index
            index += 1
        
        # Overlapping and merging intervals
        while index < n and intervals[index][0] <= newInterval[1]:
            # Calculate the new starting and ending time
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            # Increment the index
            index += 1
        
        # Add the modified newInterval
        result.append(newInterval)

        # No overlapping after merging newInterval
        while index < n:
            # Add the remaining intervals
            result.append(intervals[index])
            index += 1
        
        return result


if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    result = Solution().insert(intervals, newInterval)
    print(result)
```

## Approach 2 $(TC: O(N), SC: O(N))$
The second approach is to use binary search in place of linear search to search for the correct position to insert the newInterval into the intervals array. Once we insert the newInterval, then we iterate over the intervals and add them into our result based on the above cases (Only cases 3 and 4 are considered as because the intervals array is sorted so we don't have to worry about the start time in this approach).

**Code for this approach is given in the python file**