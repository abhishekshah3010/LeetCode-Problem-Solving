class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for s in strs:
            base = "".join(sorted(s))
            
            if base in dic:
                dic[base] += [s]
            else:
                dic[base] = [s]
        
        return dic.values()
    
    