from data_structures.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.buckets = [None] * size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            self.buckets[index] = LinkedList()
        self.buckets[index].insert((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current:
            pair = current.value
            curr_key = pair[0]
            if curr_key == key:
                return pair[1]

            current = current.next

    def contains(self, key):
        idx = self.hash(key)
        bucket = self.buckets[idx]

        if bucket is None:
            return

        current = bucket.head

        while current:
            if current.value[0] == key:
                return True

            current = current.next

    def keys(self):
        collection = set()

        for bucket in self.buckets:
            if bucket is not None:
                current = bucket.head

                while current:
                    pair = current.value
                    current_key = pair[0]
                    collection.add(current_key)
                    current = current.next

        return collection

    def hash(self, key):
        sums = 0

        if type(key) is str:
            for char in key:
                sums += ord(char)
                
        elif type(key) is int:
            sums = key
        prime = sums
        index = prime % self.size

        return index
