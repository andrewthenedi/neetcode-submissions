class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # T: O(V + E) | S: O(V + E)
        # V = Size of courses
        # E = Size of prerequisites
        course_to_prereq = collections.defaultdict(list)
        visiting = set()
        visited = set()
        course_valid_order = []
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
        def dfs(course: int) -> bool:
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in course_to_prereq[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            course_valid_order.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return course_valid_order
