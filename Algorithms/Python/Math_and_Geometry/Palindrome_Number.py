class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x_rev, a = 0, x
        while x > 0:
            lastDigit = x % 10
            x_rev = x_rev * 10 + lastDigit
            x = x // 10
        return a == x_rev
