class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, visited, root, prefix):
            if x < 0 or y < 0 or x == len(board[0]) or y == len(board): return False
            if (x, y) in visited: return False
            if board[y][x] not in root.children: return False

            visited.add((x,y))
            prefix += board[y][x]
            root = root.children[board[y][x]]

            if root.isWord:
                res.add(prefix)
                root.isWord = False
                
            visited.add((x,y))
            dfs(x+1, y, visited, root, prefix)
            dfs(x-1, y, visited, root, prefix)
            dfs(x, y+1, visited, root, prefix)
            dfs(x, y-1, visited, root, prefix)
            visited.remove((x,y))     
            
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        res = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(x, y, set(), root, "")
        return res
        
