# O(N) / O(N)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        ans = []
        queue = collections.deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            cur_level = [0] * level_size
            for i in range(level_size):
                node = queue.popleft()
                idx = i if left_to_right else level_size - i - 1
                cur_level[idx] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_to_right = not left_to_right
            ans.append(cur_level)
        return ans