class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        minutes = 0
        fresh = 0
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh += 1
                elif grid[i][j]==2:
                    q.append((i,j))

        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q and fresh>0:
            size = len(q)
            for _ in range(size):
                r,c = q.popleft()
                for dr,dc in dir:
                    nr = dr+r
                    nc = dc+c
                    if (0<= nr <n and 0<= nc <m and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            minutes += 1
        if fresh>0:
            return -1
        return minutes
