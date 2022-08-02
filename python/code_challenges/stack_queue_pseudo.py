from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.en_stack = Stack()
        self.de_stack = Stack()

    def enqueue(self, elem):
        self.en_stack.push(elem)

    def dequeue(self):  # pop out the last item using FIFO rule
        if self.de_stack.is_empty():
            while not self.en_stack.is_empty():
                self.de_stack.push(self.en_stack.pop())
        return self.de_stack.pop()


