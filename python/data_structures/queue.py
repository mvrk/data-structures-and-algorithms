from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, element, next_=None):
        self.value = element
        self.next = next_


class Queue:
    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new = Node(element, None)
        if self.is_empty():
            self.front = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("empty queue!")
        result = self.front.value
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return result

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("empty queue!")
        return self.front.value




