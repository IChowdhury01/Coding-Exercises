class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = float("-inf")
        while l < r:
            area = self.getArea(height, l, r)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

    def getArea(self, height: List[int], l: int, r: int) -> int:
        heightL, heightR = height[l], height[r]
        area = min(heightL, heightR) * (r-l)
        return area
