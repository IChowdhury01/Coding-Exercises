# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder - [3,9,20,15,7]
            always is node, then left then right
        inorder - [9,3,15,20,7]
            always left, node, right
        ans = [3,9,20,null,null,15,7]
        '''
        if not preorder and not inorder: return

        node = TreeNode(preorder[0])
        m = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:m+1], inorder[:m])
        node.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return node
