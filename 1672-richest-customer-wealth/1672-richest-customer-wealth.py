class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # return max(map(sum, accounts))
        
        #return(max([sum(i) for i in accounts]))
        
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)
            
