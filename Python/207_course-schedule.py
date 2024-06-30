from collections import defaultdict, deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = defaultdict(set)
        graph = defaultdict(set)
        for c,q in prerequisites:
            preq[c].add(q)
            graph[q].add(c)
        queue =deque()
        for i in range(numCourses):
            if not preq[i]:
                queue.append(i)
        view = []
        while queue:
            c = queue.popleft()
            view.append(c)
            if len(view)==numCourses:
                return True
            for each in graph[c]:
                preq[each].remove(c)
                if not preq[each]:
                    queue.append(each)
        return False