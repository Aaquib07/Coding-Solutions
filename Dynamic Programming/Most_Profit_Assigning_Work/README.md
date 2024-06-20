# Problem
You have `n` jobs and `m` workers. You are given three arrays: difficulty, profit, and worker where:

- `difficulty[i]` and `profit[i]` are the difficulty and the profit of the i<sup>th</sup> job, and 

- `worker[j]` is the ability of j<sup>th</sup> worker (i.e., the j<sup>th</sup> worker can only complete a job with difficulty at most `worker[j]`).

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

### Constraints
- n == difficulty.length
- n == profit.length
- m == worker.length
- 1 <= n, m <= 10<sup>4</sup>
- 1 <= `difficulty[i]`, `profit[i]`, `worker[i]` <= 10<sup>5</sup>

# Solution
## Approach 1 $(TC: O(N \cdot \log N + M \cdot \log N ), SC: O(N))$

In this approach, we create a list of tuples that contains the difficulty of a job and its profit. Then we sort the list according to difficulty in ascending order. After that, we find running maximum operation (i.e., what is the maximum of all the values till the current value) on the profits of jobs. Once its done, we iterate over every worker's ability and perform binary search to find a job that is having just smaller or equal to the ability of current worker. During binary search, we check if the difficulty at the mid index is less than or equal to the ability of the current worker, updating the maximum profit and left pointer to search in the right half in that case. Otherwise, we update the right pointer to perform search in the left half.

### Code
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Stores the total profit
        result = 0
        # Initialize a list of tuples that contains the difficulty as well as the profit
        # of a job
        jobs_info = [(di, pi) for di, pi in zip(difficulty, profit)]
        # Sort them according to the difficulty of a job in ascending order
        jobs_info.sort()

        # Iterate through every worker
        for ability in worker:
            max_profit = 0    # Stores the maximum profit for the current worker
            left = 0    # Initialize left pointer
            right = len(jobs_info) - 1    # Initialize right pointer

            # Iterate until left pointer exceeds the right pointer
            while left <= right:
                # Calculate mid index
                mid = (left + right) // 2
                
                current_difficulty = jobs_info[mid][0]

                # If the current difficulty is less or equal to the ability of worker
                if current_difficulty <= ability:
                    current_profit = jobs_info[mid][1]
                    # Update the maximum profit for the current worker
                    max_profit = max(max_profit, current_profit)
                    # Update left pointer to search in the right half
                    left = mid + 1
                else:
                    # If the current difficulty is greater than the ability or worker
                    # then update the right pointer and search in the left half
                    right = mid - 1
            
            # Add the maximum profit for the worker to the result
            result += max_profit
        
        return result


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    result = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(result)
```

## Approach 2 $(TC: O(N \cdot \log N + M \cdot \log N ), SC: O(N))$

In this approach, we create a list of tuples that contains the difficulty of a job and its profit. Then we sort the list according to profit in descending order. After that, we find running minimum operation (i.e., what is the minimum of all the values till the current value) on the difficulty of jobs. Once its done, we iterate over every worker's ability and perform binary search to maximize the total profit. During binary search, we check if the difficulty at the mid index is less than or equal to the ability of the current worker, updating the maximum profit and right pointer to search in the right half to possibly get a higher profit job in that case. Otherwise, we update the left pointer to perform search in the left half.

### Code
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Stores the total profit
        result = 0
        # Initialize a list of tuples that contains the profit as well as the difficulty
        # of a job
        jobs_info = [(pi, di) for pi, di in zip(profit, difficulty)]
        # Sort them according to the profit of a job in descending order
        jobs_info.sort(reverse=True)

        # Iterate through every worker
        for ability in worker:
            max_profit = 0    # Stores the maximum profit for the current worker
            left = 0    # Initialize left pointer
            right = len(jobs_info) - 1    # Initialize right pointer

            # Iterate until left pointer exceeds the right pointer
            while left <= right:
                # Calculate mid index
                mid = (left + right) // 2
                
                current_difficulty = jobs_info[mid][1]

                # If the current difficulty is less or equal to the ability of worker
                if current_difficulty <= ability:
                    current_profit = jobs_info[mid][0]
                    # Update the maximum profit for the current worker
                    max_profit = max(max_profit, current_profit)
                    # Update right pointer to search in the left half
                    right = mid - 1
                else:
                    # If the current difficulty is greater than the ability or worker
                    # then update the left pointer and search in the right half
                    left = mid + 1
            
            # Add the maximum profit for the worker to the result
            result += max_profit
        
        return result


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    result = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(result)
```

## Approach 3 $(TC: O(N \cdot \log N + M \cdot \log M ), SC: O(N))$

In this approach, we again create a list of tuples that contains the difficulty of a job as well as the corresponding profit. We sort the list according to the difficulty in ascending order. Then we sort the abilities of workers in ascending order. We initialize a variable `max_profit` to store the maximum profit for a worker. Then we iterate through each of the worker and check whether the current job's difficulty is less than or equal to the current worker's ability, updating the maximum profit that can be otained by the current worker in that case and iteratively check for all the possible jobs. Lastly, we add the maximum profit into the result.

### Code
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Store the total profit
        result = 0

        # Intitialize a list of tuples that contains the difficulty as
        jobs_info = [(di, pi) for di, pi in zip(difficulty, profit)]

        # Sort them according to difficulty
        jobs_info.sort()

        # Sort the worker ability in ascending order
        worker.sort()

        # Stores the maximum profit
        max_profit = 0

        # Pointer that points to the jobs list
        index = 0

        # Iterate through every worker ability
        for ability in worker:
            # Iterate until index exceeds the length of job_info or
            # difficulty exceeds the ability of a worker
            while index < len(jobs_info) and jobs_info[index][0] <= ability:
                current_profit = jobs_info[index][1]
                # Update the maximum profit
                max_profit = max(max_profit, current_profit)
                # Increment the index
                index += 1

            # Update the result
            result += max_profit 
        
        return result


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    result = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(result)
```

## Approach 4 $(TC: O(M \cdot \log N + M \cdot \log M ), SC: O(N))$

In this approach, In this approach, we again create a list of tuples that contains the difficulty of a job as well as the negative of the corresponding profit (because we are going to build max-heap). Then we heapify the list and build a max-heap. We sort the abilities of the workers in descending order. Then we iterate through all the workers and for each worker we find whether there are some jobs that are having difficulty exceeding the ability of the worker, popping all those jobs in that case. Then we check if some jobs are remaining, adding the corresponding profits into the result.

### Code
```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Stores the total profit
        result = 0
        # Initialize a list of tuples that contains the difficulty of a job as well as the negative of the corresponding profit
        jobs_info = [(-pi, di) for pi, di in zip(profit, difficulty)]
        # Build a max-heap of the list
        heapify(jobs_info)

        # Sort the abilities of workers in descending order
        worker.sort(reverse=True)

        # Iterate through every worker
        for ability in worker:
            # Until the jobs_info max-heap is non-empty and the difficulty of the job is greater than the ability of the worker
            while jobs_info and jobs_info[0][1] > ability:
                # Pop the jobs from the max-heap
                heappop(jobs_info)
            
            # If there are elements in the max-heap
            if jobs_info:
                # Add the profits into the result
                result += -jobs_info[0][0]
        
        return result


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    result = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(result)
```

## Approach 5 $(TC: O(M + N + MaxAbility ), SC: O(MaxAbility))$

In this approach, we initialize a list `jobs` consisting of `max_ability` (maximum of all abilities of worker) entries. Each index represents the maximum profit obtained for abilities ranging from 0 to `max_ability` (inclusive). Then we iterate through every job difficulties and check if the job difficulty is less than or equal to `max_ability`, updating the corresponding job difficulty entry in the `jobs` list to the maximum of previous profit and current profit. In this way, we don't need to consider all the job difficulties that are greater than `max_ability`. After that, we perform running maximum operation to calculate the maximum profit obtained by any worker having ability in range 0 to `max_ability`. Lastly, we just run a loop to add the profits into the result.

**Code for this approach is given in the python file**