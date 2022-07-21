"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        
        stack = [node]
        clones = {node:Node(node.val)}
        
        while stack:
            curr = stack.pop()
            
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    stack.append(nei)
                clones[curr].neighbors.append(clones[nei])
        return clones[node]
        