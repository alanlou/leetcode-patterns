# O(N) / O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCA_recu(root):
            if not root:
                return None
            if root == p or root == q:
                return root

            left, right = LCA_recu(root.left), LCA_recu(root.right)
            if left and right:
                return root
            return left or right
            
        return LCA_recu(root)