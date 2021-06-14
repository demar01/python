
from typing import Collection
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)

        for course, pre in prerequisites:
            adjList[pre].append(course) #from this prerequisives we can go to our courses

        def cycle(node, tracker, visited):  #helper method to detect if there is a cycle
            tracker[node] = True # yes we have been here
            visited[node] = True # yes we have been here
            for n in adjList[node]:
                if n not in visited and cycle(n,tracker, visited): #if we have been here or we continue or deep search
                    return True
                elif n in tracker:
                    return True
            tracker.pop(node)
            return False
        visited= {}
        for n in range(numCourses): #traverse our entire list of course and check if there is a cycle or not. 
            tracker= {}
            if n not in visited and cycle(n, tracker, visited):
                return False
        
        return True

#cycle detection problem
#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/


#represent our prerequisites in a directed graph. Detect if any cycle exist. If it does return False

#dfs recursively and track with nodes you already visited. pop off what from the recursive track which nodes you arleady visited

# numCourses = 2; prerequisites = [[1,0]]