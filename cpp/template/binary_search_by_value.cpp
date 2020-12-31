class Solution {
    // Template 1. bisect_lo
    //     return the smallest m such that g(m) is true
    // O(log(r-l)) / O(1)
    int bisect_lo(vector<int>& nums, int target) {
        // l is min possible value
        // r is max possible value + 1
        int l = 0, r = 10e5;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (g(m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    // Template 2. bisect_hi
    //     return the largest m such that g(m) is true
    // O(log(r-l)) / O(1)
    int bisect_hi(vector<int>& nums, int target) {
        // l is min possible value - 1
        // r is max possible value
        while (l < r) {
            int m = r - (r - l) / 2;
            if (g(m)) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        return l;
    }
};