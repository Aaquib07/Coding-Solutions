from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(i: int, j: int) -> int:
            left = i
            right = j

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            distance = right - left - 1
            return distance

        n = len(s)
        left_pointer, right_pointer = 0, 0
        for i in range(n):
            odd_length = expandFromCenter(i, i)
            if odd_length > right_pointer - left_pointer + 1:
                distance = odd_length // 2
                left_pointer = i - distance
                right_pointer = i + distance
            
            even_length = expandFromCenter(i, i + 1)
            if even_length > right_pointer - left_pointer + 1:
                distance = (even_length // 2) - 1
                left_pointer = i - distance
                right_pointer = i + 1 + distance
        
        return s[left_pointer : right_pointer + 1]


if __name__ == '__main__':
    s = 'aacabdkacaa'
    result = Solution().longestPalindrome(s)
    print(result)