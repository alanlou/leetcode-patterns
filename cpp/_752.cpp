// O(10000) / O(10000)
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        
        queue<string> q;
        q.push("0000");
        unordered_set<string> visited(deadends.begin(), deadends.end());
        
        int steps = 0;
        while (!q.empty()) {
            int level_size = q.size();
            for (int i = 0; i < level_size; ++i) {
                string cur = q.front(); q.pop();
                if (cur == target)
                    return steps;
                if (visited.find(cur) != visited.end())
                    continue;
                visited.insert(cur);
                for (string &nxt : get_successors(cur)) {
                    q.push(std::move(nxt));
                }      
            }
            ++steps;
        }
        
        return -1;
    }
private:
    vector<string> get_successors(string cur) {
        vector<string> ans;
        for (int i = 0; i < 4; ++i) {
            string tmp = cur;
            tmp[i] = (cur[i] - '0' + 1) % 10 + '0';
            ans.push_back(tmp);
            tmp[i] = (cur[i] - '0' - 1 + 10) % 10 + '0';
            ans.push_back(tmp);
        }
        return ans;
    }
};