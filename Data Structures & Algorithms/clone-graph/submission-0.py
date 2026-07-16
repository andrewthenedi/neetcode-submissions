"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = collections.defaultdict(lambda: Node())
        def recursive(node: Optional['Node']) -> Optional['Node']:
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node].val = node.val
            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(recursive(neighbor))
            return old_to_new[node]
        return recursive(node)
