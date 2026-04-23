class Solution:
    # this is a topological sort problem!
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list (really it's a map)
        course_to_prereq = { c: [] for c in range(numCourses) }

        for crs, pre in prerequisites:
            course_to_prereq[crs].append(pre)
        
        # courses can be in 3 possible states

        # visted -> crs has been added to output

        # visiting -> crs not added to output but it's in the current path

        # unvisted -> not in path or output

        res = [] # courses we can take from no pre-reqs to most pre-reqs
        
        visited = set()
        current_path = set()

        def dfs(node):
            if node in current_path:
                return False
            
            if node in visited:
                return True

            current_path.add(node)
            for pre in course_to_prereq[node]:
                if dfs(pre) == False:
                    return False
            
            current_path.remove(node) # we finished this path and made it to this point so we can remove it from the current path
            visited.add(node) # we officially can add this course to our output so this node is fully visited
            res.append(node) # add it to the output
            return True

        
        for c in range(numCourses):
            if dfs(c) == False:
                return [] # only return empty if dfs returns False at any point

        return res # else we made it all the way through!