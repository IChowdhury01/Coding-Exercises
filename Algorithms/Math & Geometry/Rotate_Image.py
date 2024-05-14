class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0])-1
        while l <= r:
            t, b = l, r
            for i in range(r-l):
                temp = [matrix[t][l+i], matrix[t+i][r], matrix[b][r-i], matrix[b-i][l]]
                print(temp)
                matrix[t][l+i] = temp[3]
                matrix[t+i][r] = temp[0]
                matrix[b][r-i] = temp[1]
                matrix[b-i][l] = temp[2]
            l += 1
            r -= 1
        return matrix
