class Solution:
    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        result = math.inf
        ones = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # perform BFS
                    # if all ones are found, update result
                    # else just continue 
                    dist = 0
                    one_count = ones
                    q = deque()
                    visited = set()
                    q.append((i,j))
                    visited.add((i,j))
                    path = 0
                    while len(q) > 0:
                        n = len(q)
                        path += 1
                        while n > 0:
                            n -= 1
                            top = q.popleft()
                            # check child nodes 
                            r, c = top
                            # up
                            if r > 0 and (r-1, c) not in visited:
                                visited.add((r-1, c))
                                if grid[r-1][c] == 0:
                                    q.append((r-1, c))
                                elif grid[r-1][c] == 1:
                                    dist += path
                                    one_count -= 1
                            # down
                            if r < len(grid)-1 and (r+1, c) not in visited:
                                visited.add((r+1, c))
                                if grid[r+1][c] == 0:
                                    q.append((r+1, c))
                                elif grid[r+1][c] == 1:
                                    dist += path
                                    one_count -= 1
                            # left
                            if c > 0 and (r, c-1) not in visited:
                                visited.add((r, c-1))
                                if grid[r][c-1] == 0:
                                    q.append((r, c-1))
                                elif grid[r][c-1] == 1:
                                    dist += path
                                    one_count -= 1
                            # right
                            if c < len(grid[0])-1 and (r, c+1) not in visited:
                                visited.add((r, c+1))
                                if grid[r][c+1] == 0:
                                    q.append((r, c+1))
                                elif grid[r][c+1] == 1:
                                    dist += path
                                    one_count -= 1
                    if one_count == 0:
                        result = min(result, dist)
            
        if result == math.inf:
            return -1 
        return result
