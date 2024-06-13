from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = [0, 0]

        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                result = [i, i + 1]
        
        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    result = [i, j]
        
        i, j = result
        return s[i:j + 1]


if __name__ == '__main__':
    s = 'babad'
    result = Solution().longestPalindrome(s)
    print(result)