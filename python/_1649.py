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
    def createSortedArray(self, instructions: List[int]) -> int:
        ans, MOD = 0, 10**9 + 7
        fw_tree = FenwickTree(max(instructions))
        
        for i, num in enumerate(instructions):
            left = fw_tree.query(num - 1)
            right = i - fw_tree.query(num)
            ans = (ans + min(left, right)) % MOD
            fw_tree.update(num, 1)
            
        return ans