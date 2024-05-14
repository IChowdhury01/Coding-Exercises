class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
    
        visited = set()
        
        def dfs(course):
            if adj[course] == []: return True
            if course in visited: return False
            
            visited.add(course)
            for prereq in adj[course]:
                completable = dfs(prereq)
                if not completable: return False
            adj[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
