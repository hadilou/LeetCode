

class Solution:
    def dfs(self,grid,i,j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1" :
            # stop searching
            return
        grid[i][j] = "s"
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i+1,j)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # marked as seen
                    self.dfs(grid,i,j)
                    # count only when you are stopped from traversing the graph
                    count+=1
        return count           
                    

        