# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        Reverse Inorder Traversal. Count sum while traversing. Replace current value with current sum. Return root at the end.
        O(N) Time, 1 pass. O(LogN) Average Space, O(N) Worst Space
        Python: Nonlocal. When doing modification on a global data structure (append(), add(), pop()), nonlocal is not needed. When doing assignment on a global variable (=, +=, -=), nonlocal is needed. 
        '''

        curSum = 0
        def dfs(root):
            nonlocal curSum
        
            if not root:
                return
            
            dfs(root.right)
            curSum += root.val
            root.val = curSum
            dfs(root.left)
        dfs(root)
        return root
