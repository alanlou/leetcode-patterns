// O(logN) / O(1)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target)
                return m;
            if (nums[m] > nums[l]) {
                if (nums[l] <= target && target < nums[m])
                    r = m;
                else
                    l = m + 1;
            } else {
                if (nums[m] < target and target <= nums[r - 1])
                    l = m + 1;
                else
                    r = m;
            }
        }
        return -1;
    }
};