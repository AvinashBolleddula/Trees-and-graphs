# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base case, if no root return []
        if not root:
            return []
        # BFS done with queue in iterative approach here
        # go level by level, after removing all elements for a level, new level nodes should filled there in queue
        # you can do BFS with recursion also
        queue = deque([root])
        right_view = []
        while queue:
            nodes_in_current_level  = len(queue)
            right_view.append(queue[-1].val)
            # Before entering for loop, the queue has level nodes everytime here, so we take last node of every level
            # At each level remove all nodes in that level and add next level nodes
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view
            
        