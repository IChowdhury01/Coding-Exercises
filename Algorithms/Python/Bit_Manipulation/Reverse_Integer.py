class Solution:
    def reverse(self, x: int) -> int:
        '''
        We aren't allowed to create a value that requires more than 32 bits, at any point in the program. res value can't ever exceed -2^31 or 2^31-1 while it's being built. So we have to determine whether an overflow will happen early, before the last digit is appended to make it overflow.
        2 Scenarios for detecting 32-bit overflow
        1. Reversed number, at any point before completion, exceeds left digits of bound number (all digits except the rightmost digit) -> No matter what the next digit is, the result will always be too large for 32 bits.
        2. Reversed number matches Left digits of bound number + Next digit about to be appended to reversed number exceeds last digit of bound number -> Reversed number just barely exceeds the bound for 32-bits (by less than 10)

        Python: Be careful when doing any division with negative numbers in Python. It will not round towards 0. 
        Use int(a/b) instead of // and fmod(a, b) instead of a % b when dividing negatives. Or take the abs(), divide, and add back the negative at the end.
        '''

        MIN_NUM = -2 ** 31
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM_LEFT_DIGITS = int(MIN_NUM / 10)
        MAX_NUM_LEFT_DIGITS = MAX_NUM // 10
        MIN_NUM_LAST_DIGIT = fmod(MIN_NUM, 10)
        MAX_NUM_LAST_DIGIT = MAX_NUM % 10

        res = 0
        while x:
            digit = fmod(x, 10)
            x = int(x / 10)

            if res > MAX_NUM_LEFT_DIGITS or res < MIN_NUM_LEFT_DIGITS:
                return 0
            if res == MAX_NUM_LEFT_DIGITS and digit > MAX_NUM_LAST_DIGIT:
                return 0
            if res == MIN_NUM_LEFT_DIGITS and digit < MIN_NUM_LAST_DIGIT:
                return 0
            
            res = res * 10 + digit
        return int(res)
