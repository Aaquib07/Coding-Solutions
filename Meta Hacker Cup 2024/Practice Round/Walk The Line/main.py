from typing import List

class Solution:
    def walkTheLine(self, s: List[int], k: int) -> str:
        n = len(s)
        s.sort()
        total_time = max(2 * n - 3, 1) * s[0]
        if total_time <= k:
            return 'YES'
        return 'NO'


if __name__ == '__main__':
    result = []
    with open('walk_the_line_input.txt') as in_file:
        test_cases = int(in_file.readline())
        for i in range(test_cases):
            n, k = map(int, in_file.readline().strip().split())
            s = []
            for _ in range(n):
                x = int(in_file.readline())
                s.append(x)

            ans = Solution().walkTheLine(s, k)
            result.append(ans)

    with open('walk_the_line_output.txt', 'w') as out_file:
        for i, ans in enumerate(result):
            out_file.write(f'Case #{i + 1}: {ans}\n')
