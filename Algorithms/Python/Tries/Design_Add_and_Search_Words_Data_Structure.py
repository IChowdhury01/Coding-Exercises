# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.node
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(idx=0, node=self.node):
            for i in range(idx, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in node.children.values():
                        if dfs(i+1, child): return True
                    return False
                if letter not in node.children:
                    return False
                node = node.children[letter]
            return node.end_of_word
        return dfs()
