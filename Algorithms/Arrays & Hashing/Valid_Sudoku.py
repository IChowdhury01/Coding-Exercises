class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict, colDict, subDict = defaultdict(set), defaultdict(set), defaultdict(set)
        for y in range(len(board)):
            for x in range(len(board[y])):
                c = board[y][x]
                if c != ".":
                    if c in rowDict[y] or c in colDict[x] or c in subDict[(x // 3, y // 3)]:
                        return False
                    rowDict[y].add(c)
                    colDict[x].add(c)
                    subDict[(x // 3, y // 3)].add(c)
        
        return True
