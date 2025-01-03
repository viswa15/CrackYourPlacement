class Solution:

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        res = []
        v = [False] * len(adj)

        def dfs(i,res,v):
            res.append(i)
            v[i] = True

            for n in adj[i]:
                if not v[n]:
                    dfs(n,res,v)
            return


        for i in range(len(adj)):
            if not v[i]:
                dfs(i,res,v)
        return res