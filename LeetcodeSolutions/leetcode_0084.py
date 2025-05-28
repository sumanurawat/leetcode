from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        stack.append(-1)
        result = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                y = heights[stack.pop()]
                x = i-1-stack[-1]
                area = x*y
                result = max(result, area)
            stack.append(i)
        while len(stack) > 1:
            y = heights[stack.pop()]
            x = len(heights)-1-stack[-1]
            area = x*y
            result = max(result, area)
        return result

