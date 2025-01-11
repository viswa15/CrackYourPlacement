#using bfs
class Solution:
	def isBipartite(self, adj):
		#code here
        n = len(adj)
        visited = [-1] * n

        def bfs(start):
            q = [start]
            visited[start] = 0

            while q:
                cur = q.pop(0)
                for i in adj[cur]:
                    if visited[i] == -1:
                        q.append(i)
                        visited[i] = 1 - visited[cur]
                    elif visited[i] == visited[cur]:
                        return False
            return True

        for i in range(n):
            if visited[i] == -1:
                if not bfs(i):
                    return False
        return True