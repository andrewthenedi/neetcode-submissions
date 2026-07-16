"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # T: O(V + E) | S: O(E)
        # V = Size of node vertexes
        # E = Size of node edges
        old_to_new = collections.defaultdict(Node)
        def recursive(node: Optional['Node']) -> Optional['Node']:
            if node not in old_to_new:
                old_to_new[node].val = node.val
                old_to_new[node].neighbors = [recursive(neighbor) for neighbor in node.neighbors]
            return old_to_new[node]
        return recursive(node) if node else None
