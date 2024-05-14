class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while l <= r and t <= b:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1

            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1

            if not (l <= r and t <= b): break

            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1

            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        return res
