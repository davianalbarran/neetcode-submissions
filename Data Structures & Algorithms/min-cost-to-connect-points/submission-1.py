# Minimum Spanning Tree Algos:
# Kruskal's
# Prim's <- this is the one we're using

# If you need to find the minimum cost to make all points connected
# that is the telltale sign that this is a minimum spanning tree problem
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # adj list is not a part of Prim impl, but still necessary!
        N = len(points)
        adj = { i: [] for i in range(N) } # each node i mapeed to list of (cost, node)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's is similar to Dijkstra's
        visited = set()
        min_heap = [[0, 0]] # tracks the "frontier" of the nodes, AKA the next nodes that can be connected
        res = 0

        # BELOW IS PRIM'S ALGO
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, [neiCost, nei])
        
        return res
