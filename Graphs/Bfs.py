class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj):
        # code here
        res = [0]
        exp = [0]
        visited = [False] * len(adj)
        while exp:
            e = exp.pop(0)
            visited[e] = True
            for i in adj[e]:
                if not visited[i]:
                    res.append(i)
                    exp.append(i)
                    visited[i] = True

        return res
