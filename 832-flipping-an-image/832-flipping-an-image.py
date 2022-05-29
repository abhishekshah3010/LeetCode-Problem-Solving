class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[abs(y-1) for y in x][::-1] for x in image]
        # return [[0 if x==1 else 1 for x in y][::-1] for y in image] 
        
        