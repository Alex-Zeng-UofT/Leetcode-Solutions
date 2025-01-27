class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        grid = [[False] * numCourses for _ in range(numCourses)]
        ret = []
        visited = [False] * numCourses

        def copyOver(course, prereq):
            for i in range(numCourses):
                if grid[prereq][i]:
                    grid[course][i] = True

        def setPrereqs(course):
            
            if visited[course]:
                return

            visited[course] = True

            for i in range(numCourses):
                if grid[course][i]:
                    setPrereqs(i)
                    copyOver(course, i)

        for prereq, course in prerequisites:
            grid[course][prereq] = True

        for i in range(numCourses):
            setPrereqs(i)

        for prereq, course in queries:
            ret.append(grid[course][prereq])

        return ret