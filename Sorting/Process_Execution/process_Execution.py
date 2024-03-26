from typing import List
from bisect import bisect_left, bisect_right


def processExecution(power: List[int], minPower: List[int], maxPower: List[int]):
    result = []
    # Sort the power list
    sorted_power = sorted(power)
    n = len(sorted_power)

    # Precompute the prefix sum of powers of processes
    power_sum = [0] * (n + 1)
    for i in range(n):
        power_sum[i + 1] = power_sum[i] + sorted_power[i]
    
    # Iterate through each processor's power range
    for min_p, max_p in zip(minPower, maxPower):
        # Find the leftmost index of the valid processes
        left_index = bisect_left(sorted_power, min_p)

        # Find the rightmost index of the valid processes
        right_index = bisect_right(sorted_power, max_p)

        # Number of valid processes
        count = right_index - left_index
        # Total power of valid processes
        total_power = power_sum[right_index] - power_sum[left_index]
        # Add the count of valid processes and their power sum to our result
        result.append([count, total_power])
    
    return result


if __name__ == '__main__':
    power = [7, 6, 8, 10]
    minPower = [6, 3, 4]
    maxPower = [10, 7, 9]
    result = processExecution(power, minPower, maxPower)
    print(result)