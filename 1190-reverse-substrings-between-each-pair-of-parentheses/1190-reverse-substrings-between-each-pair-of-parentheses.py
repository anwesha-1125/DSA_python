class Solution:
    def reverseParentheses(self, s: str) -> str:
        arr=[]
        for i in s:
            if i is "(":
                arr.append(i)
            elif i is ")":
                temp = []
                while arr[-1]!="(":
                    temp.append(arr.pop())
                arr.pop()
                arr.extend(temp)
            else:
                arr.append(i)
        return "".join(arr)
            






       

