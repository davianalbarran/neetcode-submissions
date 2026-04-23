# Dijkstra's!!!
# Dijkstra's is BFS with a Min Heap instead of queue which we will use to find the shortest path
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time[i] = (starting node, ending node, weight of edge between them)
        adj = defaultdict(list)

        for start, end, time in times:
            adj[start].append((time, end))
        # time it takes to reach a node will be the sum of the weights of the nodes before it
        min_heap = [(0, k)] # we're starting from node k which takes 0 time to signal itself
        visited = set()
        t = 0

        # while our heap has values, let's go through them
        while min_heap:
            # get the time weight and target node in our heap
            # remember with a min heap, we will be popping the node with the smallest time
            time1, node1 = heapq.heappop(min_heap)

            # if we've been here, skip
            if node1 in visited:
                continue
            
            # else add it to visited and reset time if the node takes longer to reach
            visited.add(node1)
            t = max(t, time1)

            # go through the connected nodes like a normal BFS
            for time2, node2 in adj[node1]:
                if node2 not in visited:
                    # push child node to our min heap if we haven't been here
                    # we need to remember to add the time weights of the edges
                    # to ensure our min heap accurately tracks which paths are the longest
                    heapq.heappush(min_heap, (time1 + time2, node2))
            
        return t if len(visited) == n else -1
