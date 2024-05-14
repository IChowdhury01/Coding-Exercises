class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        cur_min = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            cur_min = min(nums[mid], nums[l], cur_min)
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        
        return cur_min
