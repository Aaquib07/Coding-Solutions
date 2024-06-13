class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Function to calculate the minimum steps to reach next key character
        def count_steps(curr_idx, next_idx):
            steps_between = abs(curr_idx - next_idx)
            steps_around = len(ring) - steps_between
            return min(steps_around, steps_between)
        
        dp = [[float('inf')] * (len(key) + 1) for _ in range(len(ring))]

        # Base case
        for ring_index in range(len(ring)):
            dp[ring_index][len(key)] = 0
        
        for key_index in range(len(key) - 1, -1, -1):
            for ring_index in range(len(ring)):
                for i in range(len(ring)):
                    if ring[i] == key[key_index]:
                        total_steps = count_steps(ring_index, i) + 1 + dp[i][key_index + 1]
                        dp[ring_index][key_index] = min(dp[ring_index][key_index], total_steps)
        
        return dp[0][0]



if __name__ == '__main__':
    ring = 'godding'
    key = 'godding'
    result = Solution().findRotateSteps(ring, key)
    print(result)