# Template 1. preorder DFS
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


# Template 2. inorder DFS
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


# Template 3. postorder DFS
# O(N) / O(H)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            arr.append(node.val)
        postorder(root)
        return arr