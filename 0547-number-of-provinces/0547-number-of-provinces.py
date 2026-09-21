class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = []
        n = len(isConnected)

        graph = defaultdict(list)
        
        for i,row in enumerate(isConnected):
            for j,val in enumerate(row):
                if val == 1:
                    graph[j].append(i)
                    graph[i].append(j)

        cnt = 0

        def dfs(node):
            visited.append(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        for i in range(n):
            if i not in visited:
                cnt+=1
                dfs(i)

        return cnt