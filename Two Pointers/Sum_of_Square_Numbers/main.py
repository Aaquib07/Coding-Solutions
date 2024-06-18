class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Initialize left and right boundary
        left, right = 0, int(c ** 0.5)
        
        # Iterate until left boundary exceeds right boundary
        while left <= right:
            a_square = left ** 2
            b_square = right ** 2

            # If the sum equals c, we return true
            if a_square + b_square == c:
                return True
            # If the sum is less than c
            elif a_square + b_square < c:
                # Increment the left boundary
                left += 1
            else:
                # Otherwise, decrement the right boundary
                right -= 1
        
        # If c cannot be obtained
        return False



if __name__ == '__main__':
    c = 5
    result = Solution().judgeSquareSum(c)
    print(result)
