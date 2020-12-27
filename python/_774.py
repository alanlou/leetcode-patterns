# O(NlogM) / O(1)
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        
        def count(d):
            ans = 0
            for i in range(1, len(stations)):
                ans += (stations[i] - stations[i-1] - 1e-6) // d
            return ans
            
        l, r = 0, stations[-1] - stations[0]
        while r - l > 1e-6:
            m = l + (r - l) / 2.0
            if count(m) <= K:
                r = m
            else:
                l = m
        return l