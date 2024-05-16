class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            # Choose a random pivot index inside your subarray
            pivot = randint(0, len(nums)-1)
            
            # Create 3 subarrays to hold values smaller, larger, and equal to your pivot value. Partition array into them.
            smaller, larger, equal = [], [], []
            for n in nums:
                if n < nums[pivot]:
                    smaller.append(n)
                elif n > nums[pivot]:
                    larger.append(n)
                else:
                    equal.append(n)
            
            S, L, E = len(smaller), len(larger), len(equal)
            if k <= L:  
                '''
                Too many values larger than Pivot. 
                Ex. If k = 1, and there's 1 value larger than pivot, pivot can't be 1st largest value in nums.
                Pivot is too small.
                Kth largest is somewhere to the right (in list of larger values)
                '''
                return quickSelect(larger, k)
            elif k > (L+E): 
                '''
                Too many values smaller than Pivot. 
                Ex. If k = 5, but there's only 3 values equal to or larger than pivot. 
                Pivot is too larger.
                Kth largest is somewhere to the left (in list of smaller values). 
                Shift k by number of values ommitted from subarray L + E
                '''
                return quickSelect(smaller, k - L - E)
            else:
                return equal[0]
        return quickSelect(nums, k)
