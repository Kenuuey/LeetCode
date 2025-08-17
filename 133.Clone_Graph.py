"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
    
        # Dictionary to keep track of cloned nodes
        old_to_new = {}
        
        def dfs(n: 'Node') -> 'Node':
            if n in old_to_new:
                return old_to_new[n]  # Return already cloned node
            
            # Clone the node
            copy = Node(n.val)
            old_to_new[n] = copy
            
            # Recursively clone neighbors
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
    
        return dfs(node)