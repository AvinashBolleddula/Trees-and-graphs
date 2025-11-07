# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Asking largest value in each row, so BFS
        # Implement BFS with queue in iterative manner and at each level initialize max_val to -inf
        # And while looping through that level, compare and get max_val of that level and add it to result array
        
        
        
        # Base case, when root is None, return []
        if not root:
            return []
        queue = deque([root])
        # Array to capture max elements in each level
        large_arr = []
        while queue:
            nodes_in_current_level = len(queue)
            # At start of each level initialize max_val to -inf
            max_val = float('-inf')
            # Loop through each element in a level and get max val in that level and append it to result array
            for _ in range(nodes_in_current_level):
                node  = queue.popleft()
                max_val = max(max_val,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            large_arr.append(max_val)
        return large_arr
        