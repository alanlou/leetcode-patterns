// O(NlogM) / O(1)
class Solution {
public:
    int maximizeSweetness(vector<int>& A, int K) {
        int l = 0, r = accumulate(A.begin(), A.end(), 0) / (K + 1), m;
        while (l < r) {
            m = r - (r - l) / 2;
            if (count(A, m) >= K + 1)
                l = m;
            else
                r = m - 1;
        }
        return l;
    }
private:
    int count(vector<int>& A, int t) {
        int ans = 0, cur = 0;
        for (auto& s : A) {
            cur += s;
            if (cur >= t) {
                ans++;
                cur = 0;
            }
        }
        return ans;
    }
};