class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n = len(image)
        m = len(image[0])
        old_color = image[sr][sc]
        if old_color == color:
                return image
        
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            if image[r][c] != old_color:
                return
            image[r][c] = color

            # Explore 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
            

        dfs(sr,sc)
        return image