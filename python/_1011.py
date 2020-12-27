# O(NlogM) / O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def count(t):
            ans, cur = 1, 0
            for w in weights:
                cur += w
                if cur > t:
                    ans += 1
                    cur = w
            return ans
        
        l, r = max(weights), sum(weights) + 1
        while l < r:
            m = l + (r - l) // 2
            if count(m) <= D:
                r = m
            else:
                l = m + 1
        return l