class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # mp = {}
        # for i in nums:
        #     if i in mp:
        #         mp[i] += 1
        #     else:
        #         mp[i] = 1
        # for i,j in mp.items():
        #     if j >= n/2:
        #         return i

        for i,j in Counter(nums).items():
             if j > n//2:
                return i
        
                