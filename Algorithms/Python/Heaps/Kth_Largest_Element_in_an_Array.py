class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        larger, equal, smaller = [], [], []

        for num in nums:
            if num > pivot:
                larger.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                equal.append(num)
        
        L, E, S = len(larger), len(equal), len(smaller)

        if L >= k: return self.findKthLargest(larger, k)
        elif (L+E) < k: return self.findKthLargest(smaller, k - L - E)
        else: return equal[0]

        
        if k <= L:
            return self.findKthLargest(larger, k)
        elif L + E < k:
            return self.findKthLargest(smaller, k - L - E)
        else: return equal[0]
