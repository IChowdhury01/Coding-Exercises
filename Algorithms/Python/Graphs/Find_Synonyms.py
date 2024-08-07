'''
Problem:
If a is a synonym of b and b is a synonym of c, this implies that a is a synonym of c and c is a synonym of a

"advice:counsel counsel:suggestion suggestion:advice activity:briskness briskness:liveliness"

In this example, advice, counsel, suggestion are all synonyms of each other, while advice is not a synonym of activity.

Problem: Given an input data in the format above and a word, write a program to find out all the synonyms of that word.


input: string of synonyms, word
string
    input always valid
    no empty string
    always at least 1 pair of words
word
    no empty string
    edge case: word not in synonym string


Convert string of synonyms -> adjacency list -> Loop adjacency list -> DFS from each node if it matches input word. Append to result list.
TC: O(N + M^2), N = Chars in string, M = Unique Words
SC: O(M)

"advice:counsel counsel:suggestion suggestion:advice activity:briskness briskness:liveliness"
briskness
[liveliness, activity]
'''

from collections import defaultdict

class Solution:
    def listSynonyms(self, pairs: str, word: str) -> list[str]:
        tokens = pairs.split(" ")

        adj = defaultdict(list)
        
        for t in tokens:
            n1, n2 = t.split(":")
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node in visited:
                return
            res.append(node)
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        res = []
        visited = set()
        
        for root in adj.keys():
            if root == word:
                dfs(root)

        return res[1:] if res else res



solution = Solution()
print(solution.listSynonyms("advice:counsel counsel:suggestion suggestion:advice activity:briskness briskness:liveliness", "briskness"))
print(solution.listSynonyms("advice:counsel counsel:suggestion suggestion:advice activity:briskness briskness:liveliness", "rock"))
print(solution.listSynonyms("advice:counsel counsel:suggestion suggestion:advice activity:briskness briskness:liveliness", "counsel"))
print(solution.listSynonyms("advice:counsel", "rock"))
print(solution.listSynonyms("advice:counsel", "counsel"))
print(solution.listSynonyms("a:b b:c c:d d:e e:f", "f"))
