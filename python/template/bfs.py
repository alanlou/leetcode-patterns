# Template 1. BFS using deque
# O(N) / O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = collections.deque([root])
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                # code here
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # return here
        return


# Template 2. BFS not using deque
# O(N) / O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        arr = [root]
        while arr:
            nxt_arr = []
            for node in arr:
                # code here
                if node.left:
                    nxt_arr.append(node.left)
                if node.right:
                    nxt_arr.append(node.right)
            arr = nxt_arr

        # return here
        return