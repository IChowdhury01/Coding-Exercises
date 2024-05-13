class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = 0, 0
        for n in nums:
            temp = max(n + two_back, one_back)
            two_back = one_back
            one_back = temp
        return one_back
