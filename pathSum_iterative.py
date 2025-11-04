class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case, tree is Null
        if not root:
            return False

        # Create a stack with tuple root and value 0 (curr)
        stack = [(root, 0)]
        # iterate until stack is empty
        while stack:
            # pop stack
            node, curr = stack.pop()
            # if both children are null, then the node is a leaf
            # check targetSum validation
            if node.left == None and node.right == None:
                if (curr + node.val) == targetSum:
                    return True

            # if atleast one child exists add value of node to curr
            # and append that child
            curr += node.val
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))

        # executes only after all stack is empty, no match, so False
        return False