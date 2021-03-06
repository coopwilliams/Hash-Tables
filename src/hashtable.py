# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        new = LinkedPair(key, value)
        # print the table so far
        print("\nTABLE SO FAR:\n")
        for i in range(self.capacity):
            sll = []
            current = self.storage[i]
            while current is not None:
                sll.append((current.key, current.value))
                current = current.next
            print(sll)
        # if there's already a Linked Pair there, append to singly linked list
        current = self.storage[index]
        if current != None:
            # replace head if it matches key
            if current.key == key:
                self.storage[index] = new
                new.next = current.next
                return
            while current.next:
                prev, current = current, current.next
                if current.key == key:
                    prev.next, new.next = new, current.next
                    return
            current.next = new
        else:
            self.storage[index] = new


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        prev = None
        current = self.storage[index]
        # look through singly linked list for key
        if current == None:
            print("key not found")
        else:
            while current.key != key:
                # keep track of previous node
                prev, current = current, current.next
            # if key is found, return value
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.storage[index] = None
            else:
                print("key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        # look through singly linked list for key
        if current != None:
            while current.key != key:
                if current.next != None:
                    current = current.next
                else:
                    break
            # if key is found, return value
            if current.key == key:
                return current.value
            else:
                return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_capacity = self.capacity
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        for i in range(old_capacity):
            current = old_storage[i]
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
