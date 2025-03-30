# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# just reverse in level order alternatively

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        if not root:
            return result 
        queue.append(root)
        reverse = True
        while len(queue) > 0:
            current_level = []
            reverse = not reverse
            n = len(queue)
            for _ in range(n):
                
                top = queue.popleft()
                print(top)
                current_level.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            if reverse:
                current_level.reverse()
        return result
