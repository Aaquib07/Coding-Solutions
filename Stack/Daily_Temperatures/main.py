from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                print(temperatures[stack[-1]])
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
        
        return result



if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    result = Solution().dailyTemperatures(temperatures)
    print(result)
