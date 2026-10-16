class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj_list = [[]for _ in range(n)]
        for u,v,w in roads:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w])
        distance = [sys.maxsize for _ in range(n)]
        ways = [0 for _ in range(n)]
        distance[0] = 0
        ways[0] = 1
        priority_queue = [[0,0]]
        while len(priority_queue) != 0:
            dist,node = heapq.heappop(priority_queue)
            for adjNode,weight in adj_list[node]:
                new_dist = dist + weight
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist   
                    heapq.heappush(priority_queue,[new_dist,adjNode])
                    ways[adjNode] = ways[node]
                elif new_dist == distance[adjNode]:
                    ways[adjNode] += ways[node] % MOD
        return ways[n - 1] % MOD                