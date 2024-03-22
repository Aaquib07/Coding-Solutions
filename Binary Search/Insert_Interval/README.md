# Problem
You are given an array of non-overlapping intervals intervals where intervals[i] = [start~i~, end~i~] represent the start and the end of the i^th^ interval and intervals is sorted in ascending order by start~i~. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start~i~ and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
**Note** that you don't need to modify intervals in-place. You can make a new array and return it.

### Constraints
- 0 <= intervals.length <= 10^4^
- intervals[i].length == 2
- 0 <= start~i~ <= end~i~ <= 10^5^
- intervals is sorted by start~i~ in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5^

# Solution
## Approach 1 (TC: O(N), SC: O(N))
The first approach is to compare the newInterval with all the intervals one by one. We compare the ending time of the interval at index i with the start time of the newInterval. If the ending time of the i^th^ index interval is less than the starting time of the newInterval, then we can add the i^th^ index interval in our result (as there is no overlap) and increment the index. But if the ending time of the newInterval is greater than the starting time of the interval at index i, then we can have several cases:

1. Starting time of the newInterval may be less than that of i^th^ index interval
2. Starting time of the i^th^ index interval may be less than that of the newInterval
3. Ending time of the newInterval may be greater than that of i^th^ index interval
4. Ending time of the i^th^ index interval may be greater than that of the newInterval

For case 1 and 2, we can take the minimum of them and initialize new start time with that value. For case 3 and 4, we can take the maximum of them and initializee new end time with that value. Then we add the resulting interval into our result. Lastly, we add rest of the intervals.

## Approach 2 (TC: O(N), SC: O(N))
The second approach is to use binary search in place of linear search to search for the correct position to insert the newInterval into the intervals array. Once we insert the newInterval, then we iterate over the intervals and add them into our result based on the above cases (Only cases 3 and 4 are considered as because the intervals array is sorted so we don't have to worry about the start time in this approach).