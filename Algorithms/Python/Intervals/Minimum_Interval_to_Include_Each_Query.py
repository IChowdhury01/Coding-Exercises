class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        sort intervals and queries
        keep intervals in a min heap sorted by size. [size, endpoint]
        loop queries
            loop intervals until you see one that starts after q
                add to heap
            loop heap and remove invalid intervals starts before q, but ends before q too
                pop
            minimum value in heap = solution to query. add to hashmap
        convert hashmap to array
        O(NLogN + QLogQ) Time
        O(N + Q) Space
        '''

        intervals.sort()
        res, i = {}, 0
        heap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                interval = intervals[i]
                size = interval[1] - interval[0] + 1
                heappush(heap, [size, interval[0], interval[1]])
                i += 1
            while heap and heap[0][2] < q:
                heappop(heap)
            res[q] = -1 if not heap else heap[0][0]
        for i in range(len(queries)):
            queries[i] = res[queries[i]]
        return queries
