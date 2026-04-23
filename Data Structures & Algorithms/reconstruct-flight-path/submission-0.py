class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # lexicographically order tickets list
        tickets.sort()

        adj = defaultdict(list)
        res = ["JFK"]

        for from_loc, to_loc in tickets:
            adj[from_loc].append(to_loc)
        
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            
            if node not in adj:
                return False
            
            temp = list(adj[node])
            for i, v in enumerate(temp):
                adj[node].pop(i)
                res.append(v)

                if dfs(v): return True

                adj[node].insert(i, v)
                res.pop()
            return False
            
        dfs("JFK")
        return res 