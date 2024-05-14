# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root: return 0

            maxPathLeft = dfs(root.left)
            maxPathRight = dfs(root.right)

            maxPathNoSplit = max(root.val, root.val + maxPathLeft, root.val + maxPathRight)
            maxPathSplit = root.val + maxPathLeft + maxPathRight

            res = max(res, maxPathSplit, maxPathNoSplit)
            return maxPathNoSplit
        
        res = float('-inf')
        dfs(root)
        return res
