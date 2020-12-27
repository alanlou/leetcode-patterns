// O(N) / O(N)
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        bool left_to_right = true;
        
        while (!q.empty()) {
            int level_size = q.size();
            vector<int> cur_level(level_size, 0);
            for (int i = 0; i < level_size; i++) {
                TreeNode* node = q.front();
                q.pop();
                int idx = left_to_right ? i : level_size - i - 1;
                cur_level[idx] = node->val;
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            left_to_right = !left_to_right;
            ans.push_back(cur_level);
        }
        
        return ans;
    }
};