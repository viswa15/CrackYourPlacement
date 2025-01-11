class Solution:

    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        visited = [False] * len(adj)
        stk = []

        def dfs(start):
            visited[start] = True
            for i in adj[start]:
                if not visited[i]:
                    dfs(i)
            stk.append(start)
            return

        for i in range(len(adj)):
            if not visited[i]:
                dfs(i)
        return stk[::-1]