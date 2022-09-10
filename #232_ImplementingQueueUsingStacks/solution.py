class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) != 1:
            self.s2.append(self.s1.pop())

        element = self.s1.pop()

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        return element

    def peek(self) -> int:
        while len(self.s1) != 1:
            self.s2.append(self.s1.pop())

        element = self.s1.pop()
        self.s1.append(element)

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        return element
        

    def empty(self) -> bool:
        if len(self.s1) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()