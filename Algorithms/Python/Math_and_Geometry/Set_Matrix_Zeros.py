class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenY, lenX = len(matrix), len(matrix[0])
        isFirstRowZero, isFirstColZero = False, False

        for y in range(lenY):
            for x in range(lenX):
                if matrix[y][x] == 0:
                    if y == 0: isFirstRowZero = True
                    if x == 0: isFirstColZero = True
                    matrix[0][x] = 0
                    matrix[y][0] = 0
        
        for y in range(1, lenY):
            for x in range(1, lenX):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0

        if isFirstRowZero:
            for x in range(lenX):
                matrix[0][x] = 0
        
        if isFirstColZero:
            for y in range(lenY):
                matrix[y][0] = 0
        
        return matrix
