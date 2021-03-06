class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = set()
        # for i in range(len(nums)):
        #     if nums[i] in s:
        #         return True
        #     s.add(nums[i])
        # return False
        
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False
        
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = 1
        return False
        