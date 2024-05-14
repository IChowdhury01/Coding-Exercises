class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def bt(idx=0, sub=[], cur_total=0):
            if cur_total > target: return
            if cur_total == target:
                ans.append(sub[:])
                return
            for i in range(idx, len(candidates)):
                bt(i, sub + [candidates[i]], cur_total + candidates[i])
        bt()
        return ans
