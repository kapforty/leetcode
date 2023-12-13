class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = self.head
        
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.deleteNode(node)
        self.insertNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.nodeMap:
            self.deleteNode(self.nodeMap[key])
            self.insertNode(node)
            self.nodeMap[key] = node
            return
        self.nodeMap[key] = node
        if self.capacity > 0:
            self.insertNode(node)
            self.capacity -= 1
        else:
            del self.nodeMap[self.head.next.key]
            self.deleteNode(self.head.next)
            self.insertNode(node)
        
    def insertNode(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def deleteNode(self, node):
        if node == self.tail:
            self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.next = node.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#["LRUCache","put","get","put","get","get"]
#[[1],[2,1],[2],[3,2],[2],[3]]
