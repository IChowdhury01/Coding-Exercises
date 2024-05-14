class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        If length of window - highest freq character >= k: window can be extended
        sliding window
        loop R to end of string
            
            get char at R
            increment count of char
            get length of window (r-l+1) - highest freq 
        '''

        freq = {}
        l = 0
        res = 0
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            winLen = r - l + 1
            maxFreq = max(maxFreq, freq[s[r]])
            while winLen - maxFreq > k:
                freq[s[l]] = freq[s[l]] - 1
                winLen -= 1
                l += 1
            res = max(res, winLen)
        return res
