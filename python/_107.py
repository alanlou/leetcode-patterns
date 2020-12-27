# O(N) / O(N)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = collections.deque([root])
        ans = []
        
        while queue:
            level_size = len(queue)
            cur_level = []
            for _ in range(level_size):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur_level)
            
        return ans[::-1]