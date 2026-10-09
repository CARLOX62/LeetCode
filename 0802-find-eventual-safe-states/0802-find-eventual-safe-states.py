class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        adj_list = [[]for _ in range(V)]
        indegree = [0] * V
        for node in range(V):
            for adjnode in graph[node]:
                adj_list[adjnode].append(node)
                indegree[node] += 1

        queue = deque()
        for node in range(V):
            if indegree[node] == 0:
                queue.append(node)
        result = []        
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjnode in adj_list[node]:
                indegree[adjnode] -= 1
                if indegree[adjnode] == 0:
                    queue.append(adjnode)
        result.sort()
        return result            