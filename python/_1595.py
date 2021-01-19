# O(M * N * 2^N) / O(M * 2^N)
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        min_arr = [min(x) for x in zip(*cost)]
        
        @cache
        def dp(i, mask):
            if i == m:
                ans = 0
                for j in range(n):
                    if not mask & (1 << j):
                        ans += min_arr[j]
                return ans
            
            ans = float('inf')
            for j in range(n):
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return ans
        
        return dp(0, 0)