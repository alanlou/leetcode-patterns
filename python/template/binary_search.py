class Solution:
    # Template 1. bisect_left
    # O(logN) / O(1)
    def bisect_left(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l

    # Template 2. bisect_right
    # O(logN) / O(1)
    def bisect_right(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l