# O(logN) / O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, self.bisect_left(nums, target + 1) - 1]
        
    def bisect_left(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l