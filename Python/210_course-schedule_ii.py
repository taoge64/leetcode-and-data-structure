from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrderSolution2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs
        # i just want to trace all node back
        preq = defaultdict(set)
        graph = defaultdict(set)
        for c, p in prerequisites:
            preq[c].add(p)
            graph[p].add(c)
        queue = deque()
        res = []
        for i in range(numCourses):
            if i not in preq:
                queue.append(i)
        taken = []
        while queue:
            c = queue.popleft()
            taken.append(c)
            if len(taken) == numCourses:
                return taken
            for cor in graph[c]:
                preq[cor].remove(c)
                if not preq[cor]:
                    queue.append(cor)
        # if you have any prerequisite not able to add, you have a cycle

            return []
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping_list = defaultdict(list)
        for c, p in prerequisites:
            mapping_list[c].append(p)
        # cycle is for along with the pass
        visit, cycle = set(), set()
        output = []

        def dfs(c):
            # if course is in a cycle, return false
            if c in cycle:
                return False
            # if course has already been visited, return True
            if c in visit:
                return True
            cycle.add(c)

            for each in mapping_list[c]:
                if not dfs(each):
                    return False
            cycle.remove(c)
            # add the course to the visited set and output list
            visit.add(c)
            output.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = sol.findOrder(numCourses, prerequisites)
    print("The order of courses is:", order)

