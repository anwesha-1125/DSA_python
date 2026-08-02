class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        sum2 = 0
        for i in range(n+1):
            sum += i
    
        for i in nums:
            sum2 += i
        
        ans = sum - sum2
        return ans