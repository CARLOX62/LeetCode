class Solution:
    def dfs(self,curr_node,graph,vis,path_vis,is_safe):
        vis[curr_node] = 1
        path_vis[curr_node] = 1
        for adjnode in graph[curr_node]:
            if vis[adjnode] == 0:
                ans = self.dfs(adjnode,graph,vis,path_vis,is_safe)
                if ans == False:
                    return False
            elif path_vis[adjnode] == 1:
                return False
        is_safe[curr_node] = 1
        path_vis[curr_node] = 0
        return True            
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        vis = [0 for _ in range(V)]
        path_vis = [0 for _ in range(V)]
        is_safe = [0 for _ in range(V)]
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i,graph,vis,path_vis,is_safe)
        result = []
        for i in range(V):
            if is_safe[i] == 1:
                result.append(i)
        return result            