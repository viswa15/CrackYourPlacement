#User function Template for python3

class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        adj = [[] for _ in range(N)]
        for i in range(P):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        visited = [False] * N
        path = [False] * N
        # print(adj)

        def dfs(start):
            visited[start] = True
            path[start] = True
            for k in adj[start]:
                if not visited[k]:
                    if dfs(k):
                        return True
                elif path[k]:
                    return True
            path[start] = False
            return False


        for i in range(N):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
