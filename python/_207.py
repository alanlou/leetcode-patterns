# Solution 1. topo sort using BFS
# O(N) / O(N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        # find all sources
        sources = [i for i in range(numCourses) if in_degree[i] == 0]
        
        # dfs
        while sources:
            nxt_sources = []
            for cur in sources:
                for nxt in graph[cur]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        nxt_sources.append(nxt)
            sources = nxt_sources
            
        return all(v == 0 for v in in_degree.values())
        

# Solution 2. topo sort using DFS
# O(N) / O(N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        # find all sources
        sources = [i for i in range(numCourses) if in_degree[i] == 0]
        
        # dfs
        while sources:
            curr = sources.pop()
            for nxt in graph[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    sources.append(nxt)
                
        return all(v == 0 for v in in_degree.values())