# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Now this is the same maxdepth of a binary tree problem
# But we use iterative approach, with the help of stacks
# With recursive approach we used postorder DFS, ie max calculation at a node done after visiting left and right child 
# But with iterative approach it is complicated to use postorder and inorder so we do preorder iterative approach (current,right,left)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case, root is Null
        if not root:
            return 0
        
        # Start a stack with (root node,depth 1) tuple) and ans = 0
        stack = [(root, 1)]
        ans = 0
        
        #until stack is empty iterate
        while stack:
            # pop the stack
            # append left and right child if present and increase depth by 1 for both
            # here if you observe in stack, we pop parents first and then right child finally last, so preorder
            # finally return ans which is depth
            # T.C IS O(N), S.C is O(N) for both iterative and recursive approach (S.C O(LOGN) for complete tree, best case)
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return ans