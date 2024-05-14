class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        water = min(maxLeft, maxRight) - height
        '''
        maxLeft = 0
        maxRight = 0
        l, r = 0, len(height)-1

        res = 0
        while l <= r:
            if maxLeft < maxRight:
                water = maxLeft - height[l]
                if water > 0: res += water
                maxLeft = max(height[l], maxLeft)
                l += 1
            else:
                water = maxRight - height[r]
                if water > 0: res += water
                maxRight = max(height[r], maxRight)
                r -= 1
        return res
