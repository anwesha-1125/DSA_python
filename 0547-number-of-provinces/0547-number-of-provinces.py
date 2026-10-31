class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if isConnected is None:
            return 0
        cnt = 0
        n = len(isConnected)
        vis = [False]*n

        def dfs(node):
            vis[node] = True
            for i in range(n):
                if isConnected[node][i] == 1 and not vis[i]:
                    dfs(i)

        for i in range(n):
            if not vis[i]:
                cnt+=1
                dfs(i)
        return cnt