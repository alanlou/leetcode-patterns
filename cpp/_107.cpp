// O(N) / O(N)
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int level_size = q.size();
            vector<int> cur_level;
            for (int i = 0; i < level_size; i++) {
                TreeNode* node = q.front();
                q.pop();
                cur_level.push_back(node->val);
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            ans.push_back(cur_level);
        }
        
        reverse(ans.begin(),ans.end());
        return ans;
    }
};