class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        loop through heights
            compare val to top val of stack. if smaller, can't continue stack height anymore
                pop from stack
                getarea
                    popped height * (cur index - popped index) 
                    update leftmost index
                update max area
            place height, leftmost index on stack
        loop through stack
            pop val, index
            getarea
                popped height * len(array)
            update max area
        return maxarea
        '''

        stack = []
        res = 0
        for i, height in enumerate(heights):
            leftmostI = i
            while stack and stack[-1][1] > height:
                poppedI, poppedH = stack.pop()
                area = poppedH * (i - poppedI)
                res = max(res, area)
                leftmostI = poppedI
            stack.append([leftmostI, height])
        while stack:
            poppedI, poppedH = stack.pop()
            area = poppedH * len(heights)
            res = max(res, poppedH * (len(heights) - poppedI))
        return res
