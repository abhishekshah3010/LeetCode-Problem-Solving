class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(set(s[i:i+3]))==3 for i in range(len(s)-2))
    
        # count = 0
        # for i in range(len(s) - 2):
        #     if len(set(s[i:i+3])) == 3:
        #         count+=1
        # return count
    
#         count = 0
#         for i in range(len(s)-2):
#             if (s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i]!= s[i+2]):
#                 count += 1
#         return count
            
                
        