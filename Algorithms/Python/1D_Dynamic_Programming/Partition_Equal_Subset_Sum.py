class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Intuition: When partitioning an array into two subsets, every value in the array has to be in either subset. 
        1. For the subsets to have the same sum, they both have to have subsetSum = sum(nums) // 2. The goal is to find a subset with have the sum of the input array.
        2. If sum(nums) is odd, it's impossible for both subsets to be equal. Ex. Sum = 11, can partition into subsets with sum 5, 6 or 4, 7, but not 5.5, 5.5.

        Brute Force: Backtracking. Generate all possible subsets while tracking sum of current subset. If it's sum(nums) // 2, you have a solution.
        TC: O(2^N) - 2 choices per node, take value or don't. Max depth = size of nums. SC: O(N).
        
        Memoization: If you pick a number to be part of a subset, the problem is reduced to a subproblem sum(nums) - val. You can store each of these in a cache and add that as a base case.
        O(N * M), where N = size of nums, M = sum(nums) // 2 = sum(nums). Max number of entries / saves in cache.

        DP: Make a DP set to hold all possible sums you can make out of any subset in the array. Loop array, take current value into current subset, find possible sums (add to every existing value in set), and add to set. If you ever find sum(nums) // 2 as a possible sum, you found a solution.
        O(N * M) Time. We're looping through array of size N, and for each value, looping through our entire set of possible sums.
        O(M) Space. Size of array = sum(nums) // 2

        Python: Can't add to a set while looping through it. Need to make a temporary set clone, add to the temporary set, then replace the old set with temp.
        '''

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set([0])
        
        for num in nums:
            dpNext = set(dp)
            for oldSum in dp:
                newSum = oldSum + num
                if newSum == target: 
                    return True
                dpNext.add(newSum)
            dp = dpNext
        return False
