class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque()
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.deque: return False
        self.deque.popleft()
        return True

    def deleteLast(self) -> bool:
        if not self.deque: return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if not self.deque: return -1
        return self.deque[0]

    def getRear(self) -> int:
        if not self.deque: return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.capacity
