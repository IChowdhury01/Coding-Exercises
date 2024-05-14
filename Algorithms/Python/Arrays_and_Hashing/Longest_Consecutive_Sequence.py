class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            if n-1 not in nums_set:
                len = 0
                val = n
                while val in nums_set:
                    len += 1
                    max_len = max(len, max_len)
                    val += 1
        return max_len
