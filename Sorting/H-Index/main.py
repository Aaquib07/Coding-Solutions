from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)    # No. of papers
        # Stores the frequency of citations
        frequencies = [0 for _ in range(n)]

        # Iterate through all the papers
        for citation in citations:
            # If the citation is greater than the no. of papers
            if citation > n:
                # Increment the frequency of the highest citation
                frequencies[n] += 1
            # Otherwise, increment the frequency of the citation
            else:
                frequencies[citation] += 1
        
        # Stores the cumulative sum of citation frequncies
        cumulativeCitation = 0
        # Iterate through the frequencies backward
        for index in range(n, -1, -1):
            # Update the cumulative sum
            cumulativeCitation += frequencies[index]
            
            # If the cumulative sum is greater than or equal to the current index, return the index
            if cumulativeCitation >= index:
                return index



if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    result = Solution().hIndex(citations)
    print(result)
