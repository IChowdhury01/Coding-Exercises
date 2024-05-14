class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        1. Loop through points - O(N)
            Calculate distance
            Append to list (distance, x, y)
        2. Heapify list - O(N)
        3. Loop heap. Pop k items and add to result - O(KLogN)
        4. Return result
        '''

        heap = []
        for p in points:
            x, y = p[0], p[1]
            dist = (x ** 2) + (y ** 2)
            heap.append((dist, x, y))
        heapify(heap)

        res = []
        for i in range(k):
            dist, x, y = heappop(heap)
            res.append((x, y))
        return res
