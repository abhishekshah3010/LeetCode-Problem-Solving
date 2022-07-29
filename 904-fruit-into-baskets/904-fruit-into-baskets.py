class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxfruit = -float('inf')
        hmap = {}
        
        for right in range(len(fruits)):
            if fruits[right] in hmap:
    
                hmap[fruits[right]] += 1
            else:
                hmap[fruits[right]] = 1
                
            while len(hmap)>2:
                hmap[fruits[left]]-=1
                
                if hmap[fruits[left]]==0:
                    del hmap[fruits[left]]
                left+=1
            
            maxfruit = max(maxfruit,right-left+1)
            
        return maxfruit
        