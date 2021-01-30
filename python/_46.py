# O(N * N!) / O(N * N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
    
        def dfs(used, path, ans):
            if len(path) == len(nums):
                ans.append(list(path))
                return
            for i in range(len(nums)):
                if used & (1 << i):
                    continue
                path.append(nums[i])
                dfs(used | (1 << i), path, ans)
                path.pop()

        dfs(0, [], ans)
        return ans