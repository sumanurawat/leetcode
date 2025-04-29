# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp_result = []
        def rec(node, x, y):
            if node:
                temp_result.append((x, y, node.val))
                rec(node.left, x-1, y+1)
                rec(node.right, x+1, y+1)
        rec(root, 0, 0)
        
        # Sort by column (x), then by row (y), then by value
        temp_result.sort()
        
        result = []
        if not temp_result:
            return result
            
        current_x = temp_result[0][0]
        current_result = []
        
        for x, y, val in temp_result:
            # If we've moved to a new column
            if x != current_x:
                result.append(current_result)
                current_result = [val]
                current_x = x
            else:
                current_result.append(val)
        
        # Don't forget to add the last group
        if current_result:
            result.append(current_result)
            
        return result
