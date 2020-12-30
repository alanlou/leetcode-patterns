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
    int createSortedArray(vector<int>& instructions) {
        int ans = 0, MOD = 1e9 + 7;
        FenwickTree fw_tree(*max_element(instructions.begin(), instructions.end()) + 1);
        
        for (int i = 0; i < instructions.size(); ++i) {
            int num = instructions[i];
            int left = fw_tree.query(num);
            int right = i - fw_tree.query(num + 1);
            ans = (ans + min(left, right)) % MOD;
            fw_tree.update(num + 1, 1);
        }
        
        return ans;
    }
};