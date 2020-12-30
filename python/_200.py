# Solution 1. BFS
# O(MN) / O(MN)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            grid[r][c] = '0'
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    bfs(r, c)
                    ans += 1
        return ans


# Solution 2. DFS - recursive
# O(MN) / O(MN)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans


# Solution 3. DFS - stack
# O(MN) / O(MN)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
            
        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = '0'
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        stack.append((nr, nc))
                        grid[nr][nc] = '0'

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans