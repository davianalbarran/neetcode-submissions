class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjacency_list = { node: [] for node in range(n) }

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for j in adjacency_list[node]:
                if j == prev: # filters out false positive cycle detections since it's an undirected graph
                    continue
                
                if not dfs(j, node):
                    return False
            return True
            
        # our visited nodes should be equal to n since all nodes need to be connected to be a tree
        # therefore we can't just check the nodes straight through with dfs since it won't
        # catch nodes without any edges connected
        return dfs(0, -1) and n == len(visited)
