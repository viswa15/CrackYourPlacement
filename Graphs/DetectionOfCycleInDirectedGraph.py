#User function Template for python3
from typing import List

class Solution:

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        def dfs(start,visited,path):
            visited[start] = True
            path[start] = True
            for i in adj[start]:
                if not visited[i]:
                    if dfs(i,visited,path):
                        return True
                elif path[i]:
                    return True

            path[start] = False
            return False

        visited = [False] * len(adj)
        path = [False] * len(adj)
        for i in range(len(adj)):
            if not visited[i]:
                if dfs(i,visited,path):
                    return True
        return False