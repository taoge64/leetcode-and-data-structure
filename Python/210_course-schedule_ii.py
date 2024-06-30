from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrderSolution2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs
        # in bfs, we are try to check if each preq is filled, if that's case add to view
        preq = defaultdict(set)
        graph = defaultdict(set)
        for c, q in prerequisites:
            preq[c].add(q)
            graph[q].add(c)
        queue = deque()
        for i in range(numCourses):
            if not preq[i]:
                # those class don't need prerequisites:
                queue.append(i)
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            if len(res) == numCourses:
                return res
            for each in graph[c]:
                preq[each].remove(c)
                if not preq[each]:
                    queue.append(each)

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

