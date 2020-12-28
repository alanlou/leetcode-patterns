# O(NlogM) / O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def count(d):
            ans, cur = 1, 0
            for num in nums:
                cur += num
                if cur > d:
                    ans += 1
                    cur = num
            return ans
        
        l, r = max(nums), sum(nums) + 1
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) <= m:
                r = mid
            else:
                l = mid + 1
        return l