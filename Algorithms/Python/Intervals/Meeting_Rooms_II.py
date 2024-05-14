class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for n1, n2 in intervals:
            start.append(n1)
            end.append(n2)
        start.sort()
        end.sort()

        res,count = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
        
