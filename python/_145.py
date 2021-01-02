# Solution 1. recursive
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


# Solution 2. iterative
#     uses right-first preorder and reverse the result.
# O(N) / O(H)
class Solution:
    def postorderTraversal(self, root):
        ans, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.right
            else:
                root = stack.pop().left
        return ans[::-1]


# Solution 3. iterative (one-pass)
# O(N) / O(N)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        seen = set()
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root in seen:
                    ans.append(root.val)
                    stack.pop()
                    root = None
                else:
                    seen.add(root)
                    root = root.right
        
        return ans