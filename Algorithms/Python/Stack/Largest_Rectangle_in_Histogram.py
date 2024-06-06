class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Use stack to reference previous columns
        If current col >= top of stack, stack col can still be extended
        If current col < top of stack: stack col can't be extended anymore. Pop, extend right to get area, and update res.
            Pop shorter cols from stack
            Calculate rectangle area (current i - popped i * min(h1, h2))
            update largest rectangle
            repeat until all shorter cols have been popped
        Trick: When pushing to stack, push earliest popped i (current i if none were popped). This is to account for extending a column backwards to cover popped columns.
        remaining cols in stack can be extended to end of array
        
        O(N) Time. 1 Pass with stack
        O(N) Space. Stack can hold up to N columns at once.
        '''

        stack = []
        res = 0
        for i, h in enumerate(heights):
            tempI = i
            while stack and stack[-1][1] > h:
                poppedI, poppedH = stack.pop()
                area = (i - poppedI) * poppedH
                res = max(res, area)
                tempI = poppedI
            stack.append((tempI, h))
        while stack:
            poppedI, poppedH = stack.pop()
            area = (len(heights) - poppedI) * poppedH

            res = max(area, res)
        return res
