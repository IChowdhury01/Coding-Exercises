class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenX, lenY = len(text1)+1, len(text2)+1
        dp = [[0 for i in range(lenX)] for j in range(lenY)]

        for y in range(lenY-2, -1, -1):
            for x in range(lenX-2, -1, -1):
                c1, c2 = text1[x], text2[y]
                if c1 == c2:
                    dp[y][x] = 1 + dp[y+1][x+1]
                else:
                    dp[y][x] = max(dp[y+1][x], dp[y][x+1])
        return dp[0][0]
