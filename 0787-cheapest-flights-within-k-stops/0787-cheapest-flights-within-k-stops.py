class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[]for _ in range(n)]
        for u,v,cost in flights:
            adj_list[u].append([v,cost])
        distance = [sys.maxsize for _ in range(n)]
        distance[src] = 0
        queue = deque()
        queue.append([0,src,0])
        while len(queue) != 0:
            step,node,cost = queue.popleft()
            for adjNode, price in adj_list[node]:
                new_cost = cost + price
                if new_cost < distance[adjNode]:
                    new_step = step + 1
                    if new_step == k + 1:
                        if adjNode != dst:
                            continue
                    distance[adjNode] = new_cost
                    queue.append([new_step,adjNode,new_cost])    
        if distance[dst] == sys.maxsize:
            return -1
        return distance[dst]    