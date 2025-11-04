# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # First this is a dfs traverse, because we need to go to leaf nodes, its depth traverse
        # And it is a preorder dfs, as when you are at node you compute curr, do targetSum checks and enter its children
        # So we create a dfs function that does preorder dfs recursively and it checks base case where root is null and also when it has only one node
        # And if not base case then it traverse recursively along left and right children

        def dfs(node, curr):
            # Base case if tree is null
            if not node:
                return False
            # Base case if tree has one node
            if node.left == None and node.right == None:
                return curr + node.val == targetSum
            # Preorder traversal after base case validation
            # First compute at parent node and check targetSum with curr and enter children
            curr += node.val
            left = dfs(node.left,curr)
            right = dfs(node.right,curr)
            return left or right

        # Call recursive function starting at root with curr value zero
        return dfs(root,0)