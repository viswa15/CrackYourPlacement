class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        res = []
        i=0
        j=-1
        c = 0
        while c<(m*n):
            j+=1
            if c==(m*n):
                break
            while j<n and not visited[i][j]:
                res.append(matrix[i][j])
                visited[i][j] = True
                j+=1
                c+=1
            j-=1
            i+=1
            if c==(m*n):
                break
            while i<m and not visited[i][j]:
                res.append(matrix[i][j])
                visited[i][j] = True
                i+=1
                c+=1
            j-=1
            i-=1
            if c==(m*n):
                break
            while j>=0 and not visited[i][j]:
                res.append(matrix[i][j])
                visited[i][j] = True
                j-=1
                c+=1
            j+=1
            i-=1
            if c==(m*n):
                break
            while i>=0 and not visited[i][j]:
                res.append(matrix[i][j])
                visited[i][j] = True
                i-=1
                c+=1
            i+=1
        return res
