# O(logN) / O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r-1]:
                    l = m + 1
                else:
                    r = m
            else:
                l += 1
        return False