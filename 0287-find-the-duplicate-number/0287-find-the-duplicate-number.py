class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i,0)+1
        for k,v in mp.items():
            if v >= 2:
                return k
        return -1