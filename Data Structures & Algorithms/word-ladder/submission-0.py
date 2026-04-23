class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # endWord is always in wordList
        # transform beginWord to endWord by going through wordList 
        # where the letters are one letter off
        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        # build an adj list of wildcard patterns that words in the list comply with
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        # once we have the adj list, we can BFS to find the shortest path to the end word
        while q:
            for i in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for adjWord in adj[pattern]:
                        if adjWord not in visited:
                            visited.add(adjWord)
                            q.append(adjWord)
            res += 1
        return 0