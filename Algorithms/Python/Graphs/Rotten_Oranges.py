class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Multisource BFS with counter for time + fresh oranges
        Loop grid
            Add all rotten orange (2) coords to q
            Count how many fresh oranges (1) there are
        Loop q
            Loop level
                Pop all fresh oranges
                Make them rotten (2)
                Decrement fresh orange count
                Add neighbors to q
                    Don't add if out of bounds, already visited, or not a fresh orange (1)
            increment counter
        Loop grid
            If you see a fresh orange, return -1
        return counter
        O(N*M) Time, O(N*M) Space
        '''

        q, time = deque(), 0
        freshCount = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1: 
                    freshCount += 1
                elif grid[y][x] == 2:
                    q.append((x,y))
        
        def addNeighbor(x,y):
            nonlocal freshCount
            if x < 0 or y < 0 or x == len(grid[0]) or y == len(grid) or grid[y][x] != 1: 
                return
            q.append((x,y))
            grid[y][x] = 2
            freshCount -= 1

        while q and freshCount:
            for i in range(len(q)):
                x, y = q.popleft()

                addNeighbor(x+1,y)
                addNeighbor(x-1,y)
                addNeighbor(x,y+1)
                addNeighbor(x,y-1)
            time += 1
        
        return time if not freshCount else -1
