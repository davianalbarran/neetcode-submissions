class Solution:
    # topological sort
    # DAGs - directed acyclical graph
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return "" # invalid because lexicographical order means that all else equal, shorter words should win
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j]) # we found the differing letter and we know word1's letter precedes it
                    break
        
        visited = defaultdict(bool)
        cycle = set()
        res = []

        # we need to do postorder dfs here because we need to traverse
        # all children before adding a node since we could end up in invalid
        # states if we go to a node from a grandparent that has already been 
        # visted by a middle ancestor node
        def dfs(node):
            if node in visited:
                return visited[node] # this will return true if the node has already been visited
            
            visited[node] = True

            for nei in adj[node]:
                if dfs(nei):
                    return True

            visited[node] = False
            res.append(node) # we do this at the end for postorder DFS
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
            
