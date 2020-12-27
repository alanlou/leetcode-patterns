// O(logN) / O(1)
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = bisect_left(nums, target);
        if (l == nums.size() || nums[l] != target)
            return {-1, -1};
        return {l, bisect_left(nums, target + 1) - 1};
    }
private:
    int bisect_left(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] >= target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
};