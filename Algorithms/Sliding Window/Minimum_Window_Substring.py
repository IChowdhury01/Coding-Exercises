class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        matches = 0
        sFreq, tFreq = {}, {}
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        minWinLen, minWinStr = float('inf'), ""

        for r in range(len(s)):
            cR = s[r]
            sFreq[cR] = sFreq.get(cR, 0) + 1
            if sFreq[cR] == tFreq.get(cR, 0): matches += 1
            # print(matches, s[l:r+1])

            while matches == len(tFreq.keys()):
                if (r-l+1) < minWinLen:
                    minWinLen = r-l+1
                    minWinStr = s[l:r+1]
                cL = s[l]
                sFreq[cL] = sFreq[cL] - 1
                if sFreq[cL] == tFreq.get(cL, 0) - 1: matches -= 1
                l += 1
            
        return minWinStr
            
