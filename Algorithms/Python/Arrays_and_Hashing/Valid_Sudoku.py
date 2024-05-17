class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        1. No repetition within any row
        2. No repetition within any column
        3. No repetition within 9 3x3 subgrids
        HashMap x -> Set of values in column x
        HashMap y -> Set of values in row y
        HashMap (x // 3, y // 3) -> Set of values in subgrid
        Loop grid
            Get value
            Check if current value is in any hashmap
                return false
            Add to sets
        return true
        '''
        cols = defaultdict(set)
        rows = defaultdict(set)
        subgrids = defaultdict(set)
        lenX, lenY = len(board[0]), len(board)
        for y in range(lenY):
            for x in range(lenX):
                val = board[y][x]
                if val == ".": continue
                subgrid = (x // 3, y // 3)
                if val in cols[x] or val in rows[y] or val in subgrids[subgrid]: return False
                cols[x].add(val)
                rows[y].add(val)
                subgrids[subgrid].add(val)
        return True
