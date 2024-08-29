# Question
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their i<sup>th</sup> paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

### Constraints
- n == `citations.length`
- 1 <= n <= 5000
- 0 <= `citations[i]` <= 1000

# Solution

## Approach 1 $(TC: O(N \cdot \log N ), SC: O(1))$
In this approach, we initially sort the `citations` array. Sorting the array enables us to efficiently determine the no. of papers having citations greater than or equal to the citation of a particular paper. Then, we start iterating through the array and then check if the no. of papers having greater citations is less than or equal to the current paper's citation. If the condition is satisfied, then h-index is `n - index` that is returned. After the iteration gets completed, if we are unable to find a valid h-index, we return 0.

### Code
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)    # No. of papers
        # Sort the citations
        citations.sort()

        # Iterate through each paper
        for index, citation in enumerate(citations):
            # If the no. of papers having citations greater than or equal to the current
            # paper becomes less than or equal to the current paper citation
            if n - index <= citation:
                # Return the h-index
                return n - index
        
        # If no h-index is found
        return 0
```

## Approach 2 $(TC: O(N), SC: O(N))$
In this approach, we just use counting sort method to optimize the time complexity. We use an array `frequencies` to store the frequency of the citations of the papers. We iterate through the papers and increment the frequency of the citation if the citation is less than or equal to the no. of paper; otherwise, we increment the frequency of the highest citation. After we have determined the frequencies of all the citations, we take the running sum of the frequencies of the citations starting from the highest citation frequency to lowest one. If at any index, the running sum becomes greater than or equals the index, we return the index.

**Code for this approach is given in the python file**