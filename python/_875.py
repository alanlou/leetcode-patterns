# O(NlogM) / O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def count(k):
            hours = 0
            for p in piles:
                hours += (p - 1 + k) // k # ceil
            return hours
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if count(m) <= H:
                r = m
            else:
                l = m + 1
        return l