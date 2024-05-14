# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.node
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode()
            cur_node = cur_node.children[letter]
        cur_node.end_of_word = True

    def search(self, word: str) -> bool:
        cur_node = self.node
        for letter in word:
            if letter not in cur_node.children: return False
            cur_node = cur_node.children[letter]
        return cur_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.node
        for letter in prefix:
            if letter not in cur_node.children: return False
            cur_node = cur_node.children[letter]
        return True
