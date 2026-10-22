class Node:
    def __init__(self, key: int = -1, value: int = -1, nxt: Node = None, prev: Node = None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.head, self.tail = Node(), Node()
        self.head.nxt, self.tail.prev = self.tail, self.head
        self.capacity = capacity

    
    def addBack(self, node: Node):
        prev = self.tail.prev
        prev.nxt, node.prev = node, prev
        node.nxt, self.tail.prev = self.tail, node

    
    def removeNode(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        node.nxt = node.prev = None


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        self.removeNode(self.key_to_node[key])
        self.addBack(self.key_to_node[key])
        return self.key_to_node[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].value = value
            self.removeNode(self.key_to_node[key])
            self.addBack(self.key_to_node[key])
        else:
            if len(self.key_to_node) == self.capacity:
                lru_node = self.head.nxt
                self.removeNode(self.key_to_node[lru_node.key])
                del self.key_to_node[lru_node.key]
            node = Node(key, value)
            self.addBack(node)
            self.key_to_node[key] = node







