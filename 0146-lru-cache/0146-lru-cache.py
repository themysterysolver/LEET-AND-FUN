class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.hash=dict()
        self.cap=0
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity

    def remove(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next

    def add(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    
    def get(self, key: int) -> int:
        if key in self.hash:
            node=self.hash[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node=self.hash[key]
            self.remove(node)
            node.val=value
            self.add(node)
        elif self.cap==self.capacity:
            lru=self.tail.prev
            self.remove(lru)
            del self.hash[lru.key]
            node=Node(key,value)
            self.hash[key]=node
            self.add(node)
        else:
            self.cap+=1
            node=Node(key,value)
            self.add(node)
            self.hash[key]=node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)