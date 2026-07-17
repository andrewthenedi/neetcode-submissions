class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # T: O(V + E) | S: O(V + E)
        # V = Size of courses
        # E = Size of prerequisites
        course_to_prereq = collections.defaultdict(list)
        visiting = set()
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
        def dfs(course: int):
            if not course_to_prereq[course]:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in course_to_prereq[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            course_to_prereq[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
