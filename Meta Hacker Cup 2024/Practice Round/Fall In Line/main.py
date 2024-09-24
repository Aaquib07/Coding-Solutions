from typing import List
from random import randint

class Solution:    
    def fallInLine(self, n: int, points: List[List[int]]):
        ROUNDS = 100
        max_score = 2

        for i in range(ROUNDS):
            num1 = randint(0, n - 1)
            num2 = randint(0, n - 1)

            while num1 == num2:
                num2 = randint(0, n - 1)
            
            score = 0
            for x, y in points:
                collinear = False

                X1 = points[num1][0] - x
                X2 = points[num2][0] - x
                Y1 = points[num1][1] - y
                Y2 = points[num2][1] - y

                if X1 * Y2 == X2 * Y1:
                    collinear = True
                
                if collinear:
                    score += 1
            
            max_score = max(max_score, score)
        
        return n - max_score
                


if __name__ == '__main__':
    result = []
    with open('fall_in_line_input.txt') as in_file:
        test_cases = int(in_file.readline())
        for i in range(test_cases):
            points = []
            n = int(in_file.readline())
            for _ in range(n):
                x, y = map(int, in_file.readline().strip().split())
                points.append([x, y])


            ans = Solution().fallInLine(n, points)
            result.append(ans)

    with open('fall_in_line_output.txt', 'w') as out_file:
        for i, ans in enumerate(result):
            out_file.write(f'Case #{i + 1}: {ans}\n')
