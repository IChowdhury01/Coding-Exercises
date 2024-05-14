class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        res = nums[0]
        for i in nums:
            if total < 0:
                total = 0
            total += i
            res = max(total, res)
        return res
