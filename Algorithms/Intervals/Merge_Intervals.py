class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            i1, i2 = intervals[i-1], intervals[i]
            if i2[0] <= i1[1]:
                intervals[i] = [min(i2[0], i1[0]), max(i1[1], i2[1])]
                print(i2)
            else:
                res.append(i1)
        res.append(intervals[-1])
        return res
