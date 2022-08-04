from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(string):
    # open_brackets_queue = Queue()
    open_brackets_stack = Stack()
    dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char == '[' or char == '{' or char == '(':
            open_brackets_stack.push(char)
        if dict.get(char):
            if not open_brackets_stack.peek():
                return False
            pop = open_brackets_stack.pop()
            if dict.get(char) != pop:
                return False
    if not open_brackets_stack.is_empty():
        return False
    return True

    #
    #         close_brackets_stack.push(char)  # Stack }])
    #     elif open_brackets_queue.is_empty or close_brackets_stack.is_empty:
    #         return False
    #
    # if len(open_brackets_queue) == len(close_brackets_stack):
    #     if close_brackets_stack.peek() == ')' and open_brackets_queue.peek() == '(':
    #         close_brackets_stack.pop()
    #         open_brackets_queue.dequeue()
    #     if close_brackets_stack.peek() == ']' and open_brackets_queue.peek() == '[':
    #         close_brackets_stack.pop()
    #         open_brackets_queue.dequeue()
    #     if close_brackets_stack.peek() == '}' and open_brackets_queue.peek() == '{':
    #         close_brackets_stack.pop()
    #         open_brackets_queue.dequeue()
    #     else:
    #         return False
    #
    #     if close_brackets_stack.is_empty() or open_brackets_queue.is_empty:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
