# Solution 1. BFS
# O(10000) / O(10000)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def get_successors(cur):
            ans = []
            for i, ch in enumerate(cur):
                num = int(ch)
                ans.append(cur[:i] + str((num - 1) % 10) + cur[i+1:])
                ans.append(cur[:i] + str((num + 1) % 10) + cur[i+1:])
            return ans
        
        queue = collections.deque(['0000'])
        visited = set(deadends)
        
        steps = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.popleft()
                if cur == target:
                    return steps 
                if cur in visited:
                    continue
                visited.add(cur)
                queue.extend(get_successors(cur))
            steps += 1
        
        return -1


# Solution 2. A* search
# O(10000) / O(10000)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def get_successors(cur):
            ans = []
            for i, ch in enumerate(cur):
                num = int(ch)
                ans.append(cur[:i] + str((num - 1) % 10) + cur[i+1:])
                ans.append(cur[:i] + str((num + 1) % 10) + cur[i+1:])
            return ans
        
        def get_dist(cur):
            d = 0
            for i, ch in enumerate(cur):
                d1 = abs(int(ch) - int(target[i]))
                d2 = abs(10 - d1)
                d += min(d1, d2)
            return d
        
        
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1
        
        heap = [(0, 0, '0000')]
        visited = deadends | set(['0000'])
        
        
        while heap:
            d, step, cur = heapq.heappop(heap)
            if cur == target:
                return step
            for nxt in get_successors(cur):
                if nxt in visited:
                    continue
                visited.add(nxt)
                heapq.heappush(heap, (step + 1 + get_dist(nxt), step + 1, nxt))
        
        return -1