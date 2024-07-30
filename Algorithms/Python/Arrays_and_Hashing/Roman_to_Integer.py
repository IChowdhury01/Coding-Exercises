class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToVal = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        res = 0
        for i in range(len(s)):
            # Compare curChar and nextChar values. If nextChar is larger, subtract curChar's value. Else add it.
            val = symbolToVal[s[i]]
            valNext = symbolToVal[s[i+1]] if i+1 < len(s) else 0
            if val >= valNext:
                res += val
            else:
                res -= val
        return res
