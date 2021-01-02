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
    int reversePairs(vector<int>& nums) {
        // compress
        set<long long> st(nums.begin(), nums.end());
        for (auto& num : nums)
            st.insert(2L * num);
        unordered_map<long long, int> rank;
        int i = 0;
        for (auto& num : st)
            rank[num] = ++i;
        
        int ans = 0;
        FenwickTree fw_tree(rank.size());
        for (int i = nums.size() - 1; i >= 0; --i) {
            long long num = nums[i];
            ans += fw_tree.query(rank[num] - 1);
            fw_tree.update(rank[num * 2], 1);
        }
        return ans;
    }
};