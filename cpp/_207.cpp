// topo sort using BFS
// O(N) / O(N)
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // constuct graph
        vector<vector<int>> graph(numCourses);
        vector<int> in_degree(numCourses, 0), sources;
        for (auto& e : prerequisites){
            graph[e[1]].push_back(e[0]);
            in_degree[e[0]]++;
        }
        
        // find all sources
        for (int i = 0; i < numCourses; ++i) 
            if (!in_degree[i]) sources.push_back(i);
        
        // bfs
        int cnt = 0;
        while (!sources.empty()) {
            vector<int> nxt_sources;
            for (int cur : sources) {
                cnt++;
                for (int nxt : graph[cur]) {
                    if (--in_degree[nxt] == 0)
                        nxt_sources.push_back(nxt);
                }
            }
            sources = nxt_sources;
        }
        
        return cnt == numCourses;
    }
};


// topo sort using DFS
// O(N) / O(N)
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // constuct graph
        vector<vector<int>> graph(numCourses);
        vector<int> in_degree(numCourses, 0), sources;
        for (auto& e : prerequisites){
            graph[e[1]].push_back(e[0]);
            in_degree[e[0]]++;
        }
        
        // find all sources
        for (int i = 0; i < numCourses; ++i) 
            if (!in_degree[i]) sources.push_back(i);
        
        // dfs
        int cnt = 0;
        while (!sources.empty()) {
            cnt++;
            int cur = sources.back();
            sources.pop_back();
            for (int nxt : graph[cur]) {
                if (--in_degree[nxt] == 0)
                    sources.push_back(nxt);
            }
        }
        
        return cnt == numCourses;
    }
};