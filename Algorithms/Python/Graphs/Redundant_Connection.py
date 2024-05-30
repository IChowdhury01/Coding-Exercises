class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Use union find
        If the union of two nodes returns False / 0, the two nodes are already part of the same component, so an edge can't be drawn. This means that edge is redundant and part of a cycle.
        Check union result for every edge. Return the first redundant edge you find (guaranteed to be 1)
        
        Union Find is basically rebuilding a graph by starting with each node as an isolated, separate component, then looping through edges and drawing them between components.
        Find(node) finds the component the node is in and returns the root node of that component.
        Union(node1, node2) attempts to draw an edge between the components of two nodes. If the edge is redundant (components are already connected) or part of a cycle, it will return False / 0. Everytime a union is performed, the number of components decreases by 1 (can track with counter while doing unions).

        O(N) Time. Union find does N union() operations, which amortizes to O(N).
        O(N) Space. Rank and Parent arrays are size N.
        '''

        parent = [i for i in range(len(edges)+1)]
        comp = [1] * (len(edges)+1)

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2: return 0
            if treeSize[r1] > treeSize[r2]:
                treeSize[r1] += treeSize[r2]
                parent[r2] = r1
            else:
                treeSize[r2] += treeSize[r1]
                parent[r1] = r2
            return 1
        
        res = []
        for n1, n2 in edges:
            if union(n1, n2) == 0:
                return [n1, n2]
