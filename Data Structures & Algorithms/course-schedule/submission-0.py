class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph 
        # check if there are cycles in the graph, if there are no cycles
        # possible to finish all courses

        # use DFS
        course_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            course_map[crs].append(pre)
        
        visiting = set() # all courses along curr DFS path

        def dfs(crs):
            if crs in visiting:
                # cycle detected
                return False
            if course_map[crs] == []:
                # course has no prerequisites, def can be completed
                return True

            visiting.add(crs)
            # loop through prerequisites 
            for pre in course_map[crs]:
                # one prereq that cant be completed will return false
                if not dfs(pre):
                    return False
            # no longer visiting this course
            # if u dont remove it becomes
            # visited = {0}
            # visited = {0, 1}
            # visited = {0, 1, 2}
            # which is running dfs on the same nodes again and again 
            visiting.remove(crs)
            course_map[crs] = [] # course def can be done so no need dfs on neighbors
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True