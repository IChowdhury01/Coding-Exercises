# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def search(self, word: str) -> bool:
        def dfs(i, cur):
            nonlocal word
            for j in range(i, len(word)):
                # print(word, i, j)
                c = word[j]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(j+1, child): return True
                    return False
                elif c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
            return cur.isWord
        return dfs(0, self.root)
