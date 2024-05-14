class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lenY, lenX = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(x, y):
            nonlocal maxArea
            if x < 0 or x == lenX or y < 0 or y == lenY:
                return 0
            if (x,y) in visited or grid[y][x] == 0:
                return 0

            visited.add((x,y))
            right = dfs(x+1,y)
            left = dfs(x-1,y)
            down = dfs(x,y+1)
            up = dfs(x,y-1)
            area = 1 + right + left + up + down
            maxArea = max(maxArea, area)
            return area

        for y in range(lenY):
            for x in range(lenX):
                dfs(x, y)
        return maxArea
