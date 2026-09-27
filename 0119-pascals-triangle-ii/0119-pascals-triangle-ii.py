class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr = []
        for i in range(rowIndex+1):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = arr[i-1][j-1] + arr[i-1][j]
            arr.append(row)
        return arr[-1]

        