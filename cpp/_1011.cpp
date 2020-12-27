// O(NlogM) / O(1)
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D) {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(), 0);
        while (l < r) {
            int m = l + (r - l) / 2;
            if (count(weights, m) <= D)
                r = m;
            else
                l = m + 1;
        }
        return l;
    }
private:
    int count(vector<int>& weights, int t) {
        int ans = 1, cur = 0;
        for (auto& w : weights) {
            cur += w;
            if (cur > t) {
                ans++;
                cur = w;
            }
        }
        return ans;
    }
};