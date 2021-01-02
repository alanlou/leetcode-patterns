# Solution 1. recursive
# O(N) / O(H)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        return arr


# Solution 2. iterative
# O(N) / O(H)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right
        return ans