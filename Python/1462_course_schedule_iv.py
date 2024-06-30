from collections import defaultdict
from typing import List
from functools import cache
class Solution:
    def checkIfPrerequisite_2(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #o(numCourses+p) SINCE EVERY NODE AND PRE only process once in DFS, so sum them
        preq = defaultdict(set)
        reachable = [set() for _ in range(numCourses)]
        for c,q in prerequisites:
            preq[c].add(q)
            # reachable[c].add(q)
        def check(c):
            if reachable[c]:
                return
            for each in preq[c]:
                    check(each)
                    reachable[c].add(each)
                    reachable[c].update(reachable[each])
            return
        res = []
        for p1,p2 in queries:
            if not reachable[p1]:
                check(p1)
            res.append(p2 in reachable[p1])
        return res
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #dfs to track back all potential parent pre
        preq = defaultdict(set)
        for c,p in prerequisites:
            preq[c].add(p)

        @cache
        def check(n,target):
            nonlocal preq
            if n==target:
                return True
            for e in preq[n]:
                if check(e,target):
                    return True
            return False
        res = []
        for each in queries:
            res.append(check(each[0],each[1]))
        return res
if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    queries=[[0,1],[1,0]]
    res = sol.checkIfPrerequisite(numCourses, prerequisites,queries)
    print("The result is:", res)