// O(NlogM) / O(1)
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int l = *max_element(nums.begin(), nums.end());
        int r = accumulate(nums.begin(), nums.end(), 0);
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (count(nums, mid) <= m)
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
private:
    int count(vector<int>& nums, int d) {
        int ans = 1, cur = 0;
        for (auto& num : nums) {
            cur += num;
            if (cur > d) {
                ans ++;
                cur = num;
            }
        }
        return ans;
    }
};