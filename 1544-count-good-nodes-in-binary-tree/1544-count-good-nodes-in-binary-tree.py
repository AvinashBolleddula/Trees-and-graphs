# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,curr):
            good  = 0
            if not node:
                return 0
            if node.left == None and node.right == None and node.val >= curr:
                return 1
            if node.val >= curr:
                curr = node.val
                good += 1
            left = dfs(node.left,curr)
            right = dfs(node.right,curr)

            return left + right + good
    
        return dfs(root,root.val)
        