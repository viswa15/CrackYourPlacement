from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        def bfs(start,adj,visited):
            q = [(start,-1)]
            visited[start] = True

            while q:
                curr,parent = q.pop(0)
                for i in adj[curr]:
                    if not visited[i]:
                        q.append((i,curr))
                        visited[i] = True
                    elif i != parent:
                        return True
            return False



        n = len(adj)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                if bfs(i,adj,visited):
                    return True
        return False