class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        INF = sys.maxsize
        # build adjacency matrix
        dist = [[INF] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for i in range(n):
            dist[i][i] = 0

        # Floyd-Warshall triple loop
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != INF and dist[via][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])

        # count reachable neighbors
        min_cnt, city = n + 1, -1
        for i in range(n):
            cnt = sum(dist[i][j] <= distanceThreshold for j in range(n))
            # ≥ keeps the larger index on ties
            if cnt <= min_cnt:
                min_cnt, city = cnt, i
        return city