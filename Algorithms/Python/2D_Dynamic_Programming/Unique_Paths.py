class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        oldRow = [1] * (n)
        for y in range(m-2, -1, -1):
            newRow = [1] * (n)
            for x in range(len(newRow)-2, -1, -1):
                newRow[x] = newRow[x+1] + oldRow[x]
            oldRow = newRow
                    
        return oldRow[0]
