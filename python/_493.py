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
    def reversePairs(self, nums: List[int]) -> int:
        # compress
        all_nums = set(nums + [x * 2 for x in nums])
        ranks = {num: i + 1 for i, num in enumerate(sorted(list(all_nums)))}
        
        ans = 0
        fw_tree = FenwickTree(len(ranks))
        for i in range(len(nums) - 1, -1, -1):
            ans += fw_tree.query(ranks[nums[i]] - 1)
            fw_tree.update(ranks[nums[i] * 2], 1)
            
        return ans