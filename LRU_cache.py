class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    TC: O(1)
    AS: O(capacity) - space taken by HashMap
    """

    def __init__(self, capacity: int): 
        self.map = {} # {int: node}
        self.capacity = capacity

        # Dummy nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        # Connection of dummy nodes for DLL
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node):
        # set Head as MRU
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # TC : O(1)
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value
    
    # TC : O(1)    
    def put(self, key: int, value: int) -> None:
        ### isfresh node ??
        # not fresh - replace the value for the key, then remove the node and move to head as MRU
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
        # fresh
        else:
            if self.capacity == len(self.map):
                # Remove LRU from the tail
                tailPrev = self.tail.prev
                self.removeNode(tailPrev)
                del self.map[tailPrev.key]
            newNode = Node(key, value)
            self.map[key] = newNode
            self.addToHead(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)