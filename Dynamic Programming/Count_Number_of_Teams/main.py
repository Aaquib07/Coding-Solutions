from typing import List

class Solution:
    def _countIncreasingTeams(self, rating: List[int], index: int, team_size: int, increasing_cache: List[List[int]]) -> int:
        n = len(rating)

        # Base case: end of array
        if index == n:
            return 0
        
        # Base case: found a valid team
        if team_size == 3:
            return 1
        
        if increasing_cache[index][team_size] != -1:
            return increasing_cache[index][team_size]
        
        valid_teams = 0

        for next_index in range(index + 1, n):
            if rating[next_index] > rating[index]:
                valid_teams += self._countIncreasingTeams(rating, next_index, team_size + 1, increasing_cache)
        
        increasing_cache[index][team_size] = valid_teams
        return valid_teams
    

    def _countDecreasingTeams(self, rating: List[int], index: int, team_size: int, decreasing_cache: List[List[int]]) -> int:
        n = len(rating)

        # Base case: end of array
        if index == n:
            return 0
        
        # Base case: found a valid team
        if team_size == 3:
            return 1
        
        if decreasing_cache[index][team_size] != -1:
            return decreasing_cache[index][team_size]
        
        valid_teams = 0

        for next_index in range(index + 1, n):
            if rating[next_index] < rating[index]:
                valid_teams += self._countDecreasingTeams(rating, next_index, team_size + 1, decreasing_cache)
        
        decreasing_cache[index][team_size] = valid_teams
        return valid_teams
    

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        for index in range(n):
            increasing_count = self._countIncreasingTeams(rating, index, 1, increasing_cache)
            decreasing_count = self._countDecreasingTeams(rating, index, 1, decreasing_cache)
            result += increasing_count + decreasing_count
        
        return result


if __name__ == '__main__':
    rating = [2, 5, 3, 4, 1]
    result = Solution().numTeams(rating)
    print(result)
