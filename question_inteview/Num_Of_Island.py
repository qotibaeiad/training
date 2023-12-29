class Island:
    def __init__(self, matrix):
        self.matrix = matrix

    def Num_Of_Island(self):
        cnt = 0
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        for i in range(rows):
            for j in range(columns):
                if self.matrix[i][j] == '1':
                    cnt += 1
                    self.dfs(i, j)
        return cnt
    
    
    def dfs(self,i,j):
	    rows=len(self.matrix[0])
	    columns=len(self.matrix)
	    if(0<=i<columns and 0<=j<rows and self.matrix[i][j]=='1'):
		    self.matrix[i][j]='0'
		    self.dfs(i+1,j)
		    self.dfs(i-1,j)
		    self.dfs(i,j+1)
		    self.dfs(i,j-1)

	
Matrix = [
    ['1', '1', '1', '0', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['0', '0', '1', '1', '1']
]
M = Island(Matrix)
print(M.Num_Of_Island())