// O(NlogM) / O(1)
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        while (l < r) {
            int m = l + (r - l) / 2;
            if (count(piles, m) <= H)
                r = m;
            else
                l = m + 1;
        }
        return l;
    }
private:
    int count(vector<int>& piles, int k) {
        int ans = 0;
        for (auto& p : piles) {
            ans += (p - 1 + k) / k; // ceil
        }
        return ans;
    }
};