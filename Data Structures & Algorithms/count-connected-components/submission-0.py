class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { node: [] for node in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for child in adj[node]:
                dfs(child)

        res = 0
        for node in adj:
            if node not in visited:
                print(node)
                dfs(node)
                res += 1
        
        return res
