class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #
        # code here
        def dfs(start,visited,path,ans):
            visited[start] = True
            path[start] = True
            for i in graph[start]:
                if not visited[i]:
                    if dfs(i,visited,path,ans):
                        return True
                elif path[i]:
                    return True

            path[start] = False
            ans.append(start)
            return False

        visited = [False] * len(graph)
        path = [False] * len(graph)
        ans = []
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i,visited,path,ans)
        return sorted(ans)