class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n^2)

        # n = len(nums)
        # for i in range(0,n,1):
        #     for j in range(i+1,n,1):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]

        # O(n)...dict

        mp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in mp:
                mp[nums[i]] = i
            else:
                return[i,mp[diff]]