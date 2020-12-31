# Template 1. topo sort using BFS
# O(N) / O(N)
class Solution:
    def canFinish(self, n, prereq):
        # construct graph
        graph = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}
        for u, v in prereq:
            graph[v].append(u)
            in_degree[u] += 1
        
        # find all sources
        sources = [i for i in range(n) if in_degree[i] == 0]
        
        # bfs
        cnt = 0
        while sources:
            nxt_sources = []
            for cur in sources:
                cnt += 1
                for nxt in graph[cur]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        nxt_sources.append(nxt)
            sources = nxt_sources
            
        return cnt
        

# Template 2. topo sort using DFS
# O(N) / O(N)
class Solution:
    def canFinish(self, n, prereq):
        # construct graph
        graph = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}
        for u, v in prereq:
            graph[v].append(u)
            in_degree[u] += 1
        
        # find all sources
        sources = [i for i in range(n) if in_degree[i] == 0]
        
        # dfs
        cnt = 0
        while sources:
            cur = sources.pop()
            cnt += 1
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    sources.append(nxt)
                
        return cnt