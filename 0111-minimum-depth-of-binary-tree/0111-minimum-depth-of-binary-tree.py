# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # min depth of a tree is minimum of min depths of (left tree, right tree subtrees) plus 1
        # so this is postorder dfs, because we get min depths of childs and then calculate min depth of tree
        def post_dfs(node):
            # Base case where tree is None
            if not node:
                return 0
            # If tree is a leaf
            if node.left == None and node.right == None:
                return 1
            left = post_dfs(node.left)
            right = post_dfs(node.right)
            # if tree has right but no left 
            # choose right depth plus 1, because this is not a leaf
            if node.left == None:
                return right + 1
             # if tree has left but no right 
            # choose left depth plus 1, because this is not a leaf
            if node.right == None:
                return left + 1
            # only when tree has both childs or it is a leaf
            return min(left,right) + 1
        return post_dfs(root)
   
        
        