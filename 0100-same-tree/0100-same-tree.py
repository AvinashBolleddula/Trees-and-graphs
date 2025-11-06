# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # To see whether two trees are same, traverse along the trees and create a list of nodes as you traverse and finally check if both lists are same
        def dfs(node):
            # Base case, when tree is None, create a list with None
            if not node:
                return [None]
            # Perform recursive dfs preorder traverse
            # this preorder checks if structure of tree is same in both as you traverse 
            left = dfs(node.left)
            right = dfs(node.right)
            # we are building a list of all nodes inside the tree at the node including itself and returning it at each node
            # so finally we will have all nodes when we are at root including root
            return left + right + [node.val]
        # checking whether list of all nodes captured at roots p and q are same
        return dfs(p) == dfs(q)
        
        


        