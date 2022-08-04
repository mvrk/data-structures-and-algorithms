from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, element, next_):
        self.value = element
        self.next = next_


class Stack:

    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.top = Node(element, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        result = self.top.value
        self.top = self.top.next
        self.size -= 1
        return result

    def peek(self):
        if self.is_empty():
            # raise InvalidOperationError("Method not allowed on empty collection")
            return None
        return self.top.value
