# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #Asking largest value in each row, so BFS
        # implement BFS with queue in iterative manner
        if not root:
            return []
        queue = deque([root])
        large_arr = []
        while queue:
            nodes_in_current_level = len(queue)
            max_val = float('-inf')

            for _ in range(nodes_in_current_level):
                node  = queue.popleft()
                max_val = max(max_val,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            large_arr.append(max_val)
        return large_arr
        