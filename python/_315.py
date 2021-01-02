class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)
        
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s
        
    def _lowbit(self, x):
        return x & -x

# O(NlogN) / O(N)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # compress
        all_nums = list(set(nums))
        rank = {val: i + 1 for i, val in enumerate(sorted(all_nums))}
        
        n = len(nums)
        ans = [0] * n
        tree = FenwickTree(n)
        for i in range(n - 1, -1, -1):
            ans[i] = tree.query(rank[nums[i]] - 1)
            tree.update(rank[nums[i]], 1)
        return ans