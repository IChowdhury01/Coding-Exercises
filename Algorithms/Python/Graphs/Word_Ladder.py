class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Make a directed graph connecting words with 1 character difference. Then do BFS until you reach endWord, or all nodes are traversed. Return 0 if you never reached endWord, otherwise return the level count.
        O(N^2 * K) Time. 
            K = length of words. N = number of words. 
            Building adjacency list is O(N * K^2), because for each word we loop through each character and then perform splicing to create our pattern. Splicing and Inner loop are both O(K). 
            Doing BFS on the graph is O(N^2 * K). BFS on fully connected graph = O(V+E) = O(V^2). We also generate patterns in O(K) time on each recursive call.
            N >> K so the BFS TC takes precendence.
        O(N * K^2) Space. Each word has length K. Each word is stored K times (for each possible pattern) in adjacency list. There are N words. 
        Python: Create a Set/Queue with initial values by passing in a list, e.g. deque([beginWord])
        '''
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        seqLen = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in adj[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                            if neighbor == endWord:
                                return seqLen + 1
            seqLen += 1
        return 0
