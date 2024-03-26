# Problem
There are `n` processes to be executed and `m` processors to execute them. The i^th^ process requires `power[i]` for execution. A processor can provide power within its range `minPower` through `maxPower`. Process `i` can be executed on process `j` if `minPower[i] <= power[j] <= maxPower[i]`.

Given the power consumption of `n` processes and the range of power consumption of `m` processors, for each processor:
- find the number of processes which can be executed on each processor.
- find the sum of power consumed by the processes that it can serve.


### Constraints
- 1 <= n <= 2 * 10^5^
- 1 <= m <= 2 * 10^5^

# Solution
## Approach 1 (TC: O(M * N), SC: O(1))
The very first solution that comes to our mind is that to iterate through all the power ranges of processors and then check for each of the powers of processes whether it lies in between the range. We then simply store the count and sum of those powers of processes in our result.

### Code
```python
from typing import List

def processExecution(power: List[int], minPower: List[int], maxPower: List[int]):
    results = []
    # Iterate through each processor's power range
    for min_p, max_p in zip(minPower, maxPower):
        # Calculate the count and sum of power for valid processes
        power_sum = 0
        count = 0
        for p in power:
            if min_p <= p <= max_p:
                power_sum += p
                count += 1
                
        # Add it to our result
        results.append([count, power_sum])
    return results
```

## Approach 2 (TC: O(N * log(N) + M * log(N)), SC: O(N))
The above approach exceeds the time limit. So, in our optimized approach, we sort the power list in non-decreasing order (`sorted_power`). Then we initialize a list `power_sum` to store prefix sum of powers of processes. The calculation of prefix sum of powers helps us to determine the sum of the powers of valid processes efficiently.

Then we iterate through the range of powers of processors and then find the leftmost index (`left_index`) in `sorted_power` using binary search where min power of current processor can be inserted to keep `sorted_power` list sorted (all the processes to the right of this index will be candidates for valid processes). Similarly, we find the rightmost index (`right_index`) in the `sorted_power` list using binary search where max power of current processor can be inserted to keep the `sorted_power` list sorted (all the processes to the left of this index will be candidates for valid processes).

Once we get those indices, we just subtract `left_index` from `right_index` to get the count of valid processes as because the first valid process appears at the `left_index` and the last valid process appears at the `right_index` (We are able to say this because `sorted_power` is sorted). Then we subtract `power_sum[left_index]` from `power_sum[right_index]` to get the total power for a particular processor. Lastly, we just add the total power and count for the current processor in our result and repaeat this process for the remaining processors.

**Code for this approach is given in the python file**