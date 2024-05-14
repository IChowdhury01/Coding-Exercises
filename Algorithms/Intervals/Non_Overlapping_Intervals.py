class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i: i[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                res += 1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        return res
