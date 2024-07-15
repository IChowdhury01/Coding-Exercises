class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        Approach 1: Sort array, traverse and check each pair. O(NLogN) Time, O(1) Space
        Approach 2: Counting Sort. 
            Array is bounded with a known range, values go from -10^6 to 10^6, so we can do counting sort.
            Counting sort produces an array of all possible values, and their frequency in O(N) time.
            O(N+M) Time, O(N) Space. N = Size of input array. M = Size of array value bounds (maxVal - minVal)
        Implementation
            Get min and max of array
            Create array counting frequency of all possible values. 
                Size = max - min + 1. arr
                count[0] = count of smallest value in arr.
            Loop arr
                Get value
                Shift left by min(arr) to get corresponding index in count array.
                Increment count by 1.
            Loop count with 2 pointers on tracking adjacent non-zero values
                if count[cur] > 1:
                    get diff abs(cur - prev)
                    compare to mindiff
                        if smaller clear result and append pair
                        if equal, add pair to result
                    update prev to cur
        '''

        minVal, maxVal = min(arr), max(arr)
        count = [0] * (maxVal - minVal + 1)
        for val in arr:
            countI = val - minVal
            count[countI] += 1
        minDiff = float('INF')
        res = []
        l = 0
        for r in range(1, len(count)):
            if count[r] > 0:
                diff = abs(r-l)
                if diff < minDiff:
                    res.clear()
                    res.append([l + minVal, r + minVal])
                    minDiff = diff
                elif diff == minDiff:
                    res.append([l + minVal, r + minVal])
                l = r
        return res
