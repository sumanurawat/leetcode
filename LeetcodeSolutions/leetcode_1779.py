import math
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_idx = -1
        valid_dist = math.inf

        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = (abs(x-points[i][0]) + abs(y-points[i][1]))
                if dist < valid_dist:
                    valid_dist = dist
                    valid_idx = i
        return valid_idx
