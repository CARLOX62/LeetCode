class Solution:
    def dfs(self,curr_ind,visited,graph,color):
        visited[curr_ind] = color
        for node in graph[curr_ind]:
            if visited[node] != -1:
                if visited[node] == color:
                    return False
            else:
                ans = self.dfs(node,visited,graph,1 - color)
                if ans == False:
                    return False
        return True                    

    def isBipartite(self, graph: list[list[int]]) -> bool:
        total_nodes = len(graph)
        visited = [-1] * total_nodes
        for index in range(total_nodes):
            if visited[index] == -1:
                ans = self.dfs(index,visited,graph,0)
                if ans == False:
                    return False
        return True                 