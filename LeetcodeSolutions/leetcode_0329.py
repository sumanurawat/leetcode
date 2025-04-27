class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def walk(lis, row, col, prev):

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                return 0
            
            if matrix[row][col] <= prev:
                return 0

            if (row, col) in lis:
                return lis[(row, col)]

            current = matrix[row][col]

            left = walk(lis, row-1, col, current)
            right = walk(lis, row+1, col, current)
            up = walk(lis, row, col-1, current)
            down = walk(lis, row, col+1, current)

            lis[(row, col)] = 1 + max(left, right, up, down)
            return lis[(row, col)]

        lis = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                walk(lis, i, j, -1)
        print(lis)
        return max(lis.values())
