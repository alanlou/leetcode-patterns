# O(N) / O(N)
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

class NumArray:
 
    def __init__(self, nums):
        self.nums = nums
        self.fw_tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self.fw_tree.update(i + 1, nums[i])
 
    def update(self, i, val):
        self.fw_tree.update(i + 1, val - self.nums[i])
        self.nums[i] = val
 
    def sumRange(self, i, j):
        return self.fw_tree.query(j + 1) - self.fw_tree.query(i)