from typing import List

class Solution:
    def lineByLine(self, n: int, p: int) -> float:
        prob = p / 100
        q = prob ** ((n - 1) / n)
        return (q - prob) * 100


if __name__ == '__main__':
    result = []
    with open('line_by_line_input.txt') as in_file:
        test_cases = int(in_file.readline())
        for i in range(test_cases):
            n, p = map(int, in_file.readline().strip().split())

            ans = Solution().lineByLine(n, p)
            result.append(ans)

    with open('line_by_line_output.txt', 'w') as out_file:
        for i, ans in enumerate(result):
            out_file.write(f'Case #{i + 1}: {ans}\n')
