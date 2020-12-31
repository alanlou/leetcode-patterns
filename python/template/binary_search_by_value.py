class Solution:
    # Template 1. bisect_lo
    #     return the smallest m such that g(m) is true
    # O(log(r-l)) / O(1)
    def bisect_lo(self, nums, target):
        # l is min possible value
        # r is max possible value + 1
        l, r = 0, 10**5
        while l < r:
            m = l + (r - l) // 2
            if g(m):
                r = m
            else:
                l = m + 1
        return l

    # Template 2. bisect_hi
    #     return the largest m such that g(m) is true
    # O(log(r-l)) / O(1)
    def bisect_hi(self, nums, target):
        # l is min possible value - 1
        # r is max possible value
        l, r = -1, 10**5 
        while l < r:
            m = r - (r - l) // 2
            if g(m):
                l = m
            else:
                r = m - 1
        return l