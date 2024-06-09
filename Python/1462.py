from collections import defaultdict
from typing import List
from functools import cache
class Solution:
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