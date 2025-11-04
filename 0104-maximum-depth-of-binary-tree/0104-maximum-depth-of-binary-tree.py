class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Here we use DFS for calculating maxdepth, dfs is traversing depth wise not breadth wise
        # DFS is one way to traverse a binary tree, other way is BFS
        # It doesnt matter if we use pre,in,post order dfs (we only traverse, wont print, so all are same)
        # To use dfs with recursion, first start calling functions recursively on left and right
        # And then think of what the problem wants (what should we should at a node wrt to subtrees) by thinking of last node as an example (for max depth at a node, we need left and right subtree maxdepth and add 1)
        # finally think of base case of recursion, empty tree

        
        # Base case of recursion, empty tree depth 0
        if root is None:
            return 0
        else:
            # recursively traverse left and right subtrees
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            # what to do at a node wrt to problem statement
            return max(left_height, right_height) + 1