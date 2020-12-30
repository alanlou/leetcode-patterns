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

// Solution 1. Binary Index Tree (Fenwick Tree)
// O(NlogN) / O(N)
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        
        // construct presum
        vector<long long> p(n + 1, 0);
        for (int i = 0; i < n; ++i)
            p[i + 1] = p[i] + nums[i];
        
        // sort presum array for binary searching
        sort(p.begin(), p.end());
        
        // BIT stores the index of sorted presum (from 1)
        FenwickTree fw_tree(n + 1);
        
        // sum up the number of valid presums for each presum
        int ans = 0;
        long long cur = 0;
        fw_tree.update(lower_bound(p.begin(), p.end(), 0) - p.begin() + 1, 1);
        for (int i = 0; i < n; ++i) {
            cur += nums[i];
            int left = lower_bound(p.begin(), p.end(), cur - upper) - p.begin();
            int right = upper_bound(p.begin(), p.end(), cur - lower) - p.begin();
            ans += (fw_tree.query(right) - fw_tree.query(left));
            fw_tree.update(lower_bound(p.begin(), p.end(), cur) - p.begin() + 1, 1);
        }
        
        return ans;
    }
};


// Solution 2. Divide and Conquer
// O(NlogN) / O(N)
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long> p(n + 1, 0);
        for(int i =0; i < n; ++i)
            p[i + 1] = p[i] + nums[i];
        return mergeSort(p, lower, upper, 0, n + 1);
    }
private:
    int mergeSort(vector<long>& p, int lower, int upper, int low, int high) {
        if (low + 1 >= high) return 0;

        int mid = low + (high - low) / 2;
        int ans = mergeSort(p, lower, upper, low, mid) + 
            mergeSort(p, lower, upper, mid, high);
        int l = mid, r = mid;

        for (int i = low; i < mid; ++i) {
            while (l < high && p[l] - p[i] < lower) l++;
            while (r < high && p[r] - p[i] <= upper) r++;
            ans += r - l;
        }
        inplace_merge(p.begin() + low, p.begin() + mid, p.begin() + high);
        return ans;
    }
};