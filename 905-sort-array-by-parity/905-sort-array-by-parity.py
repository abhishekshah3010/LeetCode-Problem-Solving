class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return [i for i in nums if i % 2 ==0] + [i for i in nums if i % 2 != 0]
        res = []
        for i in nums:
            if i%2==0:
                res.append(i)
        for j in nums:
            if j %2 != 0:
                res.append(j)
        return res
    
    