class Node:
    def __init__(self, val=0, count=0, prev=None, next=None):
        self.val = val
        self.count = count
        self.prev = prev
        self.next = next

class AllOne:

    def __init__(self):
        self.head = Node("", -inf)
        self.tail = Node("", inf)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeMap = {}
        

    def inc(self, key: str) -> None:
        if key not in self.nodeMap:
            new = Node(key, 1, self.head, self.head.next)
            self.head.next.prev = new
            self.head.next = new
            self.nodeMap[key] = new
        else:
            curr = self.nodeMap[key]
            curr.count += 1
            while curr.next and curr.next.count < curr.count:
                one, two, three, four = curr.prev, curr, curr.next, curr.next.next
                one.next = three
                two.next = four
                three.next = two
                four.prev = two
                three.prev = one
                two.prev = three
                curr = two

    def dec(self, key: str) -> None:
        curr = self.nodeMap[key]
        curr.count -= 1
        if curr.count == 0:
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            del self.nodeMap[key]
            return
        while curr.prev and curr.prev.count > curr.count:
            one, two, three, four = curr.prev.prev, curr.prev, curr, curr.next
            one.next = three
            two.next = four
            three.next = two
            four.prev = two
            three.prev = one
            two.prev = three
            curr = three

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return self.tail.prev.val

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return self.head.next.val


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
