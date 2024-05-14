class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posD, negD = set(), set(), set()

        res = set()
        board = [['.' for i in range(n)] for i in range(n)]
        print(board)
        
        def backtrack(r):
            if r == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                res.add(tuple(temp))

            for c in range(len(board[0])):
                if c not in cols and (r+c) not in posD and (r-c) not in negD:
                    cols.add(c)
                    posD.add(r+c)
                    negD.add(r-c)
                    board[r][c] = 'Q'
                
                    backtrack(r+1)
                
                    cols.remove(c)
                    posD.remove(r+c)
                    negD.remove(r-c)
                    board[r][c] = '.'
        
        backtrack(0)
        return res
