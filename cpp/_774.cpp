// O(NlogM) / O(1)
class Solution {
public:
    double minmaxGasDist(vector<int>& stations, int K) {
        int n = stations.size();
        double l = 0, r = stations[n - 1] - stations[0], m;
        while (r - l > 1e-6) {
            m = l + (r - l) / 2.0;
            if (count(stations, m) <= K)
                r = m;
            else
                l = m;
        }
        return l;
    }
private:
    int count(vector<int>& stations, double d) {
        int ans = 0;
        for (int i = 1; i < stations.size(); ++i) {
            ans += int((stations[i] - stations[i-1] - 1e-6) / d);
        }
        return ans;
    }
};