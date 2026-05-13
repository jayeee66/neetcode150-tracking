# Doubly Linked List

class Node:
    # Define a doubly linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Create dummy head and tail nodes, then connect them together
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next =  next_node
        next_node.prev = prev_node

    def insert_to_head(self, node):
        # Insert the node between dummy head and first node
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key already exists, delete the old node reference
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create and insert the new node as Most Recently Used
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert_to_head(new_node)

        # Handle eviction if cache exceeds the allowed capacity
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            # Important: also remove the key from the hash map
            del self.cache[lru_node.key]

        
