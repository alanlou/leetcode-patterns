// O(N * N!) / O(N * N!)
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ans;
        dfs(nums, 0, path, ans);
        return ans;
    }
private:
    void dfs(vector<int>& nums, int used, vector<int>& path, vector<vector<int>>& ans) {
        if (path.size() == nums.size()) {
            ans.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (used & (1 << i))
                continue;
            path.push_back(nums[i]);
            dfs(nums, used | (1 << i), path, ans);
            path.pop_back();
        }
    }
};