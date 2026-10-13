import sys
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return -1
        distance = [[sys.maxsize for _ in range(cols)]for _ in range(rows)]
        distance[0][0] = 1
        queue = deque()
        queue.append([1,0,0])
        while len(queue) != 0:
            dist,i,j = queue.popleft()
            for x,y in[[1,0],[0,-1],[-1,0],[0,1],[-1,-1],[-1,1],[1,1],[1,-1]]:
                new_i,new_j = i + x, j + y
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] == 1:
                    continue
                dist_trav = dist + 1
                if dist_trav < distance[new_i][new_j]:
                    if new_i == rows - 1 and new_j == cols - 1:
                        return dist_trav
                    distance[new_i][new_j] = dist_trav
                    queue.append([dist_trav,new_i,new_j])
        if distance[rows - 1][cols - 1] == sys.maxsize:
            return -1
        return distance[rows - 1][cols - 1]                                