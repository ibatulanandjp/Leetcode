class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map for key:node

        # Left: LRU, Right: MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.addNodeToRight(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deleteNode(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.addNodeToRight(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.deleteNode(lru)
            del self.cache[lru.key]

    def addNodeToRight(self, node: Node) -> None:
        node.next = self.right
        node.prev = self.right.prev
        node.prev.next = node
        node.next.prev = node
    
    def deleteNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)