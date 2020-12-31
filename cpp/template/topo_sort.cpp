// Template 1. topo sort using BFS
// O(N) / O(N)
class Solution {
public:
    int canFinish(int n, vector<vector<int>>& prereq) {
        // constuct graph
        vector<vector<int>> graph(n);
        vector<int> in_degree(n, 0), sources;
        for (auto& e : prereq){
            graph[e[1]].push_back(e[0]);
            in_degree[e[0]]++;
        }
        
        // find all sources
        for (int i = 0; i < n; ++i) 
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
        
        return cnt;
    }
};


// Template 2. topo sort using DFS
// O(N) / O(N)
class Solution {
public:
    int canFinish(int n, vector<vector<int>>& prereq) {
        // constuct graph
        vector<vector<int>> graph(n);
        vector<int> in_degree(n, 0), sources;
        for (auto& e : prereq){
            graph[e[1]].push_back(e[0]);
            in_degree[e[0]]++;
        }
        
        // find all sources
        for (int i = 0; i < n; ++i) 
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
        
        return cnt;
    }
};