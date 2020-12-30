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

# Solution 1. Binary Index Tree (Fenwick Tree)
# O(NlogN) / O(N)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        
        # construct presum
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
            
        # sort presum array for binary searching
        presum.sort()
        
        # BIT stores the index of sorted presum (from 1)
        fw_tree = FenwickTree(n + 1)
        
        # sum up the number of valid presums for each presum
        ans = cur = 0
        fw_tree.update(bisect.bisect_left(presum, 0) + 1, 1)
        for i in range(n):
            cur += nums[i]
            left = fw_tree.query(bisect.bisect_left(presum, cur - upper))
            right = fw_tree.query(bisect.bisect_right(presum, cur - lower))
            ans += (right - left)
            fw_tree.update(bisect.bisect_left(presum, cur) + 1, 1)
        
        return ans


# Solution 2. Divide and Conquer
# O(NlogN) / O(N)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
            
        def merge_sort(low, high):
            if low + 1 >= high: return 0
            
            mid = low + (high - low) // 2
            ans = merge_sort(low, mid) + merge_sort(mid, high)
            l = r = mid
            
            for i in range(low, mid):
                while l < high and presum[l] - presum[i] < lower:
                    l += 1
                while r < high and presum[r] - presum[i] <= upper:
                    r += 1
                ans += r - l
            presum[low: high] = heapq.merge(presum[low: mid], presum[mid: high])
            return ans
            
        return merge_sort(0, n + 1)