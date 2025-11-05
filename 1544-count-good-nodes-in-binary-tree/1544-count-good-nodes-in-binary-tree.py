# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we need to follow dfs here because the path is from root to node
        # preorder dfs as we check if parent is good node and then enter children
        def dfs(node, max_so_far):
            # Base case root is Null
            if not node:
                return 0
            
            # Check if current node is good
            # Here good is local variable not global
            good = 1 if node.val >= max_so_far else 0
            
            # Update max_so_far for children
            # if parent is good, choose its val as max
            # else stay as it is 
            new_max = max(max_so_far, node.val)
            
            # Recurse and accumulate counts
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)
            
            # do something on subtrees after recurrsion, depending on problem
            return good + left + right
        
        # start with -inf or rrot.val not 0 to counter neg values of root node
        return dfs(root, float('-inf'))