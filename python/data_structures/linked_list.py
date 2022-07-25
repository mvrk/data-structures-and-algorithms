class Node:
    """
    Create new node object for linked list to use
    """
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

    def insert(self, value):
        # self.head = Node(value)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, key):
        current_node = self.head
        while current_node:
            if current_node.value == key:
                return True
            else:
                current_node = current_node.next
        return False

    def __str__(self):
        current = self.head
        text = ''
        while current:
            text += "{ " + current.value + " } -> "
            current = current.next
        text += "NULL"
        return text





class TargetError:
    pass


# linked_list = LinkedList()
#
# linked_list.insert("apple")
#
# linked_list.insert("banana")
# print(str(linked_list))
