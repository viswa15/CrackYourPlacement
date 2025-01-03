class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        v = [[False]*len(image[0]) for _ in range(len(image))]
        def dfs(i,j,original_color,v):
            if i<0 or j<0 or i>=len(image) or j>= len(image[0]) or image[i][j] != original_color or v[i][j]:
                return
            image[i][j] = color
            v[i][j] = True
            dfs(i,j-1,original_color,v)
            dfs(i,j+1,original_color,v)
            dfs(i-1,j,original_color,v)
            dfs(i+1,j,original_color,v)
            return

        original_color = image[sr][sc]
        dfs(sr,sc,original_color,v)
        return image