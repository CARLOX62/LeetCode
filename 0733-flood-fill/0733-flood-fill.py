class Solution:
    def dfs(self,i,j,new_color,initial_col,vis,r,c):
        if i < 0 or i >= r or j < 0 or j >= c:
            return
        if vis[i][j] != initial_col:
            return
        if vis[i][j] == new_color:
            return
        vis[i][j] = new_color
        self.dfs(i+1,j,new_color,initial_col,vis,r,c) 
        self.dfs(i,j-1,new_color,initial_col,vis,r,c)
        self.dfs(i-1,j,new_color,initial_col,vis,r,c)
        self.dfs(i,j+1,new_color,initial_col,vis,r,c)           
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        vis = deepcopy(image)
        r = len(vis)
        c = len(vis[0])
        initial_col = vis[sr][sc]
        self.dfs(sr,sc,color,initial_col,vis,r,c)
        return vis
        