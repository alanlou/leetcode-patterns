// O(N) / O(N)
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
 
class NumArray {
public:
    NumArray(vector<int> nums): nums_(std::move(nums)), fw_tree_(nums_.size()) {
        for (int i = 0; i < nums_.size(); ++i)
            fw_tree_.update(i + 1, nums_[i]);
    }
    
    void update(int i, int val) {
        fw_tree_.update(i + 1, val - nums_[i]);
        nums_[i] = val;
    }
    
    int sumRange(int i, int j) {
        return fw_tree_.query(j + 1) - fw_tree_.query(i);
    }
private:
    vector<int> nums_;
    FenwickTree fw_tree_;
};