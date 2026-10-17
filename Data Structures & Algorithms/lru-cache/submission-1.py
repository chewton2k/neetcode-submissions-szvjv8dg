class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): 
        node.prev.next = node.next 
        node.next.prev = node.prev

    def insert(self, node):
        previous = self.right.prev 
        previous.next = node
        node.prev = previous 
        node.next = self.right 
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key] 
            node.value = value
            self.remove(node)
            self.insert(node)
            return 

        newNode = Node(key, value) 
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap: 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
