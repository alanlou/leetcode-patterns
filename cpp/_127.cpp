// O(N) / O(N)
class Solution {
public:
    int ladderLength(string begin_word, string end_word, vector<string>& word_list) {
        
        // construct word map
        unordered_map<string, vector<string>> word_map;
        for (const string &word : word_list) {
            for (size_t i = 0; i < word.size(); ++i) {
                string tmp_word = word;
                tmp_word[i] = '*';
                word_map[tmp_word].push_back(move(word));
            }
        }
        
        // prep bfs
        unordered_set<string> seen;
        queue<string> q;
        q.push(begin_word);
        int level = 0;
        
        // bfs
        while (!q.empty()) {
            int level_size = q.size();
            level++;
            for (int i = 0; i < level_size; ++i) {
                const string curr_word = q.front();
                q.pop();
                for (int j = 0; j < curr_word.size(); ++j) {
                    string tmp_word = curr_word;
                    tmp_word[j] = '*';
                    auto it = word_map.find(tmp_word);
                    if (it == word_map.cend())
                        continue;
                    for (const string &word : it->second) {
                        if (word == end_word)
                            return level + 1;
                        if (seen.count(word))
                            continue;
                        q.push(word);
                        seen.insert(word);
                    }
                }
            }
        }
        
        return 0;
    }
};