# Solution 1. recursive
# O(N) / O(H)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def preorder(node):
            if not node:
                return
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return arr


# Solution 2. iterative
# O(N) / O(H)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                root = stack.pop().right
        return ans