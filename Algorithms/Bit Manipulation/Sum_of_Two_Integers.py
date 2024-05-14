class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask, max = 0xFFFFFFFF, 0x7FFFFFFF
        while b != 0:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = sum, carry
        return a if a < max else ~(a ^ mask)
