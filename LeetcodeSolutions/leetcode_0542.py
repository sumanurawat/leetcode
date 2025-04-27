from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        
        distance = 0

        while len(q) > 0:
            distance += 1
            n = len(q)
            for _ in range(n):
                row, col = q.popleft()
                next_cells = [
                    (row+1, col),
                    (row-1, col),
                    (row, col+1),
                    (row, col-1),
                ]

                for row, col in next_cells:
                    if row >= 0 and row < len(mat) and col >= 0 and col < len(mat[0]) and (row, col) not in visited:
                        mat[row][col] = distance
                        visited.add((row, col))
                        q.append((row, col))
        return mat
