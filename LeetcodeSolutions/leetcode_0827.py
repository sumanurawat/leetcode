class Solution:

    def mark_island(self, grid, i, j, island_id):
        from collections import deque
        q = deque()
        # mark start immediately
        grid[i][j] = island_id
        size = 1
        q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    # mark *before* enqueueing
                    grid[nx][ny] = island_id
                    size += 1
                    q.append((nx, ny))
        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        island_id = 2
        island_size = {}
        # 1) label all islands
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island_size[island_id] = self.mark_island(grid, i, j, island_id)
                    island_id += 1

        # 2) base result = 1 (flip a zero into a 1)
        result = 1

        # 3) if we had any islands, maybe we already have a bigger one (all 1's case)
        if island_size:
            result = max(result, max(island_size.values()))

        # 4) try flipping each zero
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    neigh = set()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        x, y = i+dx, j+dy
                        if 0 <= x < n and 0 <= y < m and grid[x][y] > 1:
                            neigh.add(grid[x][y])
                    # sum _all_ distinct adjacent islands, then +1 for this flip
                    total = sum(island_size[k] for k in neigh)
                    result = max(result, total + 1)
        return result