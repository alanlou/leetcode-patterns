# O(NlogM) / O(1)
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        
        def count(t):
            ans = cur = 0
            for s in sweetness:
                cur += s
                if cur >= t:
                    ans += 1
                    cur = 0
            return ans
        
        l, r = 0, sum(sweetness) // (K + 1)
        while l < r:
            m = r - (r - l) // 2
            if count(m) >= K + 1:
                l = m
            else:
                r = m - 1
        return l