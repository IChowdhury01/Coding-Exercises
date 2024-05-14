class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2: return nums
        q = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            numR = nums[r]
            while q and q[-1][0] < numR:
                q.pop()
            q.append([numR, r])

            if r - l + 1 == k:
                res.append(q[0][0])

                if q[0][1] == l:
                    q.popleft()
                l += 1
        return res
            
