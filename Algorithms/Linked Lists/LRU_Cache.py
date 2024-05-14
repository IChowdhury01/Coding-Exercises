# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    '''
    Linked Hash Map
    Doubly Linked List LRU_PLACEHOLDER -- LRU_NODE -- MRU_Node -- MRU_PLACEHOLDER
    HashMap
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}  # map key to node

        self.lru, self.mru = ListNode(0, 0), ListNode(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def insertList(self, newNode: ListNode) -> None:
        newNode.next = self.mru
        newNode.prev = self.mru.prev
        self.mru.prev.next = newNode
        self.mru.prev = newNode
    

    def removeList(self, node: ListNode) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        

    def get(self, key: int) -> int:
        if key not in self.keyToNode: return -1
        self.removeList(self.keyToNode[key])
        self.insertList(self.keyToNode[key])        
        return self.keyToNode[key].val        

    def put(self, key: int, value: int) -> None:
        # If key exists, update value in dict & list node
        # If not, make node and insert to cache
            # Check if capacity is exceeded
                # Remove from linked list
                # Remove from dict
        if key in self.keyToNode:
            self.removeList(self.keyToNode[key]) 
            self.keyToNode[key].val = value
            self.insertList(self.keyToNode[key])
        else:
            newNode = ListNode(key, value)
            self.keyToNode[key] = newNode
            self.insertList(newNode)
            if len(self.keyToNode) > self.capacity:
                oldLRU = self.lru.next
                self.removeList(oldLRU)         
                del self.keyToNode[oldLRU.key]
