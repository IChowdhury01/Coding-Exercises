class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Brute Force: Generate all possible quadruplets. Check if they sum to target. O(N^4) Time, O(1) Space.
        Optimal: Sort, Recursively reduce subproblem to Two Sum II, then solve that. 
            We need to avoid duplicates in result. Best way to do that is to Sort. Then check if adjacent elements are equal while traversing array, and keep traversing if so.
            K-Sum can be reduced to 2-Sum by recursively looping through array, choosing current element (ignoring duplciates) to add to current subset sum, and calling K-1 Sum on the remainder of the array.
            Base Case: Once K = 2, we can find Two Sum for a sorted array via 2 Pointer strategy (See Two Sum II) 

            O(N^3) Time. Number of nodes per level of recursion tree = N (Each element in the array is selected during loop, like when building combinations.) Depth of recursion tree = 4 - 2 = 2. Base case Two Sum II is O(N). O(N^2) * O(N) = O(N^3)
            O(N) Space. Recursive call stack length is O(K) (keeps going until K Sum reduces to 2 Sum). Current subset array is at worst same size as input array O(N). 

            Mistake: No return statements needed. Just make result and current subset arrays outside recursive function, and backtrack appends to subset array after making the recursive call.
            Mistake: Don't forget that we have to ignore duplicates. Whenever we add an element to result or subset, compare to previous element and keep traversing if they're duplicates.
        '''
        
        nums.sort()
        res, sumset = [], []
        
        def kSum(k, target, start):
            if k == 2:
                l, r = start, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(sumset + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i-1]: 
                        continue
                    sumset.append(nums[i])
                    kSum(k-1, target - nums[i], i+1)
                    sumset.pop()       

        kSum(4, target, 0)
        return res
