from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        q.append((root, 0))
        vertical_levels = {}
        min_level = 0
        max_level = 0
        while len(q) > 0:
            top, level = q.popleft()
            min_level = min(min_level, level)
            max_level = max(max_level, level)
            if  level not in vertical_levels:
                vertical_levels[level] = []
            vertical_levels[level].append(top.val)
            if top.left:
                q.append((top.left, level-1))
            if top.right:
                q.append((top.right, level+1))
        result = []
        for key in sorted(vertical_levels.keys()):
            result.append(vertical_levels[key])
        return result