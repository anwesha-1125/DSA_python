class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        def dfs(r,c):
            if r<0 or r>= n or c<0 or c>=m:
                return
            if grid[r][c] == '0':
                return
            # Mark visited
            grid[r][c] = '0'

            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Traverse entire grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        
        return cnt