class Solution:
    def dfs(self,r,c,visited,rows,cols,grid):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 0:
            return
        if visited[r][c] == 1 and visited[r][c] == 1:
            return        
        visited[r][c] = 1
        self.dfs(r - 1,c,visited,rows,cols,grid)
        self.dfs(r,c - 1,visited,rows,cols,grid)
        self.dfs(r + 1,c,visited,rows,cols,grid)
        self.dfs(r,c + 1,visited,rows,cols,grid)
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)]for _ in range(rows)]
        queue = deque()
        # Upper Row
        r, c = 0, 0
        for c in range(cols):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, grid)

        # Last Row
        r, c = rows - 1, 0
        for c in range(cols):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, grid)

        # First Column
        r, c = 0, 0
        for r in range(rows):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, grid)

        # Last Column
        r, c = 0, cols - 1
        for r in range(rows):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, grid)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1
        return count                                                