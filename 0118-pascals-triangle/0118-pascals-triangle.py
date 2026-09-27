class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        arr=[]
        for i in range(numRows):
            r = [1]*(i+1)
            for j in range(1,i):
                r[j] = arr[i-1][j-1]+arr[i-1][j]
            arr.append(r)
        return arr
