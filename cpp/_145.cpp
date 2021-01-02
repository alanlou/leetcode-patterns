// Solution 1. recursive
// O(N) / O(H)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        postorder(root, ans);
        return ans;
    }
private:
    void postorder(TreeNode* root, vector<int>& ans) {
        if (!root) return;
        postorder(root->left, ans);
        postorder(root->right, ans);
        ans.push_back(root->val);
    }
};


// Solution 2. iterative
//     uses right-first preorder and reverse the result.
// O(N) / O(H)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        while (root || !s.empty()) {
            if (root) {
                s.push(root);
                ans.push_back(root->val);
                root = root->right;
            } else {
                root = s.top(); s.pop();
                root = root->left;
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};


// Solution 3. iterative (one-pass)
// O(N) / O(N)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        unordered_set<TreeNode*> seen;
        while (root || !s.empty()) {
            if (root) {
                s.push(root);
                root = root->left;
            } else {
                root = s.top();
                if (seen.find(root) != seen.end()) {
                    ans.push_back(root->val);
                    s.pop();
                    root = nullptr;
                } else {
                    seen.emplace(root);
                    root = root->right;
                }
            }
        }
        return ans;
    }
};