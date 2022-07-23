class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Create a linked list that:
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
    """

    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(element)  # assign new node with data value
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node.next:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{ {str(current.value)} } ->"
            current = current.next
        return output


class TargetError:
    pass
