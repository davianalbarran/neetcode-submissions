# doing something like below is doable, but there is a more graph theory-esque solution
# adj = { node: [] for node in range(1, len(edges)) } # input nodes start labeling from 1

# for n1, n2 in edges:
#     adj[n1].append(n2)
#     adj[n2].append(n1)

# visited = set()
# res = []

# def dfs(node, prev):
#     if node in visited: # cycle detected, what do we do?
#         return
    
#     for child in adj[node]:
#         if child == prev:
#             continue
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # let's solve this with union-find
        # graph theory 101: 
        # a property of trees is that if there are n nodes, then there are n - 1 edges
        # in this problem, they messed the tree up by adding 1 more edge, adding a cycle
        # this means that there are n nodes AND n edges

        # union find can tell us that we have connected two nodes that have already been connected
        # this can be used to our advantage to tell us EXACTLY what edge to remove by going edge
        # by edge in the edges list
        N = len(edges)
        parent = [i for i in range(N + 1)] # ith node -> parent (1 - n)
        rank = [1] * (N + 1)

        # two functions needed for union-find: find and union
        def find(n):
            if n == parent[n]:
                return parent[n]
            
            parent[n] = find(parent[n])
            return parent[n]
        
        # union is not fully implemented but we don't need it here
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False # we don't want the nodes to have the same parent root
            
            # the rank of a parent will determine which parent should ultimately trump
            # path compression is advanced but it helps us flatten the height of the graph
            # to determine the ultimate root parent
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2] # this will always return in this problem
        