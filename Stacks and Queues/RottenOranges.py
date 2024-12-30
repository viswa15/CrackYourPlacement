class Solution:

    #Function to find minimum time required to rot all oranges.
	def orangesRotting(self, mat):
		#Code here
		m,n = len(mat),len(mat[0])
		coordinates = []
		next = []
		sol = 0
		for i in range(len(mat)):
		    for j in range(len(mat[0])):
		        if mat[i][j] == 2:
		            coordinates.append([i,j])

		while coordinates:
		    cur = coordinates.pop()

            #down
            if cur[0] + 1 < m and mat[cur[0]+1][cur[1]] == 1:
                next.append([cur[0]+1,cur[1]])
                mat[cur[0]+1][cur[1]] = 2

            #top
            if cur[0] -1 >= 0 and mat[cur[0]-1][cur[1]] == 1:
                next.append([cur[0]-1,cur[1]])
                mat[cur[0]-1][cur[1]] = 2

            #right
            if cur[1]+1 < n and mat[cur[0]][cur[1]+1] == 1:
                next.append([cur[0],cur[1]+1])
                mat[cur[0]][cur[1]+1] = 2

            #left
            if cur[1]-1 >= 0 and mat[cur[0]][cur[1]-1] == 1:
                next.append([cur[0],cur[1]-1])
                mat[cur[0]][cur[1]-1] = 2

            if coordinates == [] and next:
                coordinates = next
                next = []
                sol += 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    return -1

        return sol