from collections import deque
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        visited = set()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                (row, col, dist) = queue.popleft()
                visited.add((row, col))
                # up
                if row-1 >=0 and (row-1, col) not in visited and rooms[row-1][col] > dist+1:
                    rooms[row-1][col] = dist+1
                    queue.append((row-1, col, dist+1))
                # down
                if row+1 < len(rooms) and (row+1, col) not in visited and rooms[row+1][col] > dist+1:
                    rooms[row+1][col] = dist+1
                    queue.append((row+1, col, dist+1))
                # left
                if col-1 >=0 and (row, col-1) not in visited and rooms[row][col-1] > dist+1:
                    rooms[row][col-1] = dist+1
                    queue.append((row, col-1, dist+1))
                # right
                if col+1 < len(rooms[0]) and (row, col+1) not in visited and rooms[row][col+1] > dist+1:
                    rooms[row][col+1] = dist+1
                    queue.append((row, col+1, dist+1))
