# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def post_dfs(node):
            if not node:
                return 0
            if node.left == None and node.right == None:
                return 1
            left = post_dfs(node.left)
            right = post_dfs(node.right)
            return max(left,right) + 1
        depth  = post_dfs(root)


        queue = deque([root])
        ans = 0
        length = 0
        while queue:
            nodes_in_current_level = len(queue)
            length += 1
            if length == depth:
                for node in queue:
                    ans += node.val
            for _ in range(nodes_in_current_level):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
        return ans
        