from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    current_a = a.head
    current_b = b.head
    # if both a and b have nodes, traverse the following:
    while current_a and current_b:
        # call insert_after method, insert b node after a node
        a.insert_after(current_a.value, current_b.value)
        # current node of ll a change to next
        current_a = current_a.next
        # if next node of ll a exists
        if current_a.next:
            current_a = current_a.next
        current_b = current_b.next
    # if a is empty, return b; otherwise return a
    if current_a is None or current_b is None:
        if current_b:
            return b
        if current_a:
            return a

    return a
