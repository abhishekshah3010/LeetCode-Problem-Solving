class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        
        e, o = 0, 0
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = even[e]
                e+=1
            else:
                nums[i] = odd[o]
                o+=1
        
        return nums
                
                
        
        
        