class FenwickTree {    
public:
    FenwickTree(int n): sums_(n + 1, 0) {}
    
    void update(int i, int delta) {
        while (i < sums_.size()) {
            sums_[i] += delta;
            i += lowbit(i);
        }
    }
    
    int query(int i) const {        
        int sum = 0;
        while (i > 0) {
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }
private:
    static inline int lowbit(int x) { return x & (-x); }
    vector<int> sums_;
};

// O(NlogN) / O(N)
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        // compress
        set<int> st(nums.begin(), nums.end());
        unordered_map<int, int> rank;
        int i = 0;
        for (int num : st)
            rank[num] = ++i;
        
        int n = nums.size();
        vector<int> ans(n, 0);
        FenwickTree fw_tree(n);
        for (int i = n - 1; i >= 0; --i) {
            ans[i] = fw_tree.query(rank[nums[i]] - 1);
            fw_tree.update(rank[nums[i]], 1);
        }
        return ans;
    }
};