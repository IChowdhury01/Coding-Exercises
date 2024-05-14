class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        DP
        array of length s + 1
        dp[0] = num ways to decode empty string = 1
        dp[1] = num ways to decode first char = 1 if 1-9, 0 otherwise
        dp[2] = take last two digits if valid + take last digit if valid = dp[i-2] + dp[i-1]
        '''
        if s and s[0] == "0": return 0
        two_back = 1
        one_back = 1 if 0 <= int(s[0]) <= 9 else 0
        for i in range(2, len(s)+1):
            one_digit = int(s[i-1])
            two_digits = int(s[i-2 : i])

            temp = 0
            if 1 <= one_digit <= 9: temp += one_back
            if 10 <= two_digits <= 26: temp += two_back

            two_back = one_back
            one_back = temp
            
        return one_back
