class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            shiftedBit = bit << (31-i)
            res = res | shiftedBit
        return res
