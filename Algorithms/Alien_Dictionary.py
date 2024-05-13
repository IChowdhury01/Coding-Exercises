class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []
        def top(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for neighbor in adj[c]:
                cycleFound = top(neighbor)
                if cycleFound: return True

            visited[c] = False
            res.append(c)

            return False
        
        for c in adj.keys():
            if top(c): return ""
        res.reverse()
        return "".join(res)
