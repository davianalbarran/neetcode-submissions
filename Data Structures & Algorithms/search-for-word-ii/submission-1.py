class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()

        for word in words:
            trie.add(word)
        
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)
        