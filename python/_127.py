# Solution 1. BFS
# O(N) / O(N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # construct word dict
        word_len = len(beginWord)
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)
                
        # bfs prep
        queue = collections.deque()
        queue.append(beginWord)
        seen = set()
        level = 0
        
        # bfs
        while queue:
            level_size = len(queue)
            level += 1
            for _ in range(level_size):
                curr_word = queue.popleft()
                for i in range(word_len):
                    temp = curr_word[:i] + '*' + curr_word[i+1:]
                    for word in word_dict[temp]:
                        if endWord == word:
                            return level + 1
                        if word not in seen:
                            seen.add(word)
                            queue.append(word)
        
        return 0


# Solution 2. two-way BFS
# O(N) / O(N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # construct word dict
        word_len = len(beginWord)
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)
                
        # bfs prep
        queue = collections.deque()
        queue.append(beginWord)
        queue.append(endWord)
        seen = {beginWord: 1, endWord: -1}
        
        # bfs
        while queue:
            cur_word = queue.popleft()
            level = seen[cur_word]
            for i in range(word_len):
                temp = cur_word[:i] + '*' + cur_word[i+1:]
                for word in word_dict[temp]:
                    if word not in seen:
                        seen[word] = level + 1 if level > 0 else level - 1
                        queue.append(word)
                    if (seen[word] > 0) ^ (level > 0):
                        return abs(seen[word] - level)
                    
        return 0