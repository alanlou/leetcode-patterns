// Template 1. preorder DFS
// O(N) / O(H)
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        preorder(root, ans);
        return ans;
    }
private:
    void preorder(TreeNode* root, vector<int>& ans) {
        if (!root) return;
        ans.push_back(root->val);
        preorder(root->left, ans);
        preorder(root->right, ans);
    }
};


// Template 2. inorder DFS
// O(N) / O(H)
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        inorder(root, ans);
        return ans;
    }
private:
    void inorder(TreeNode* node, vector<int>& ans) {
        if (!node) return;
        inorder(node->left, ans);
        ans.push_back(node->val);
        inorder(node->right, ans);
    }
};


// Template 3. postorder DFS
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