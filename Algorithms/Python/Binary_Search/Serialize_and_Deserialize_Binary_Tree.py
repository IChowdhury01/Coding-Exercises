# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            nonlocal res
            if not root: 
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)   
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(",")
        def dfs():
            nonlocal tokens, i
            if tokens[i] == "N":
                i += 1
                return None

            node = TreeNode(int(tokens[i]))
            i += 1
            
            node.left = dfs()
            node.right = dfs()
            return node
        i = 0
        return dfs()
