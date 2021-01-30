# O(C(N, K) * K) / O(C(N, K) * K)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(s, path):
            if len(path) == k:
                ans.append(list(path))
                return
            for i in range(s, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()
        
        
        dfs(1, [])
        return ans