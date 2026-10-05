class Solution:
    def dfs(self,i,j,visited,grid):
        rows = len(grid)
        cols = len(grid[0])
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if grid[i][j] == '0':
            return
        if visited[i][j] == 1:
            return
        visited[i][j] = 1
        self.dfs(i+1,j,visited,grid)
        self.dfs(i,j+1,visited,grid)
        self.dfs(i-1,j,visited,grid)
        self.dfs(i,j-1,visited,grid)
                   
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[0 for _ in range(cols)]for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and visited[r][c] == 0:
                    count += 1
                    self.dfs(r,c,visited,grid)
        return count            

