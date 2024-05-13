class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
        Word = 'AAB'
        '''
        ROWS, COLS = len(board), len(board[0])
        visited, DIRECTIONS = set(), [[0,1],[1,0],[0,-1],[-1,0]]

        def in_bounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def bt(r, c, wIdx= 0, s=''):
            if not in_bounds(r, c) or (r, c) in visited or wIdx >= len(word) or board[r][c] != word[wIdx]: return
            if wIdx == len(word) - 1:
                return True

            visited.add((r, c))

            for dx, dy in DIRECTIONS:
                nx, ny = r + dx, c + dy
                if in_bounds(nx, ny) and (nx, ny) not in visited:
                    if bt(nx, ny, wIdx + 1, s + board[r][c]): return True
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if bt(r, c): return True
        
        return False
