from collections import OrderedDict


class LRUCache:
    class LinkedList:
        def __init__(self, val, key):
            self.val = val
            self.key = key
            self.next = None
            self.last = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.LinkedList(-1, -1)
        self.tail = self.LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.last = self.head
        self.m = {}

    def addNode(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def deleteNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            resNode = self.m[key]
            resNode.val = value
            self.deleteNode(resNode)
            del self.m[key]
        else:
            if self.capacity == 0:
                del self.m[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
            else:
                self.capacity -= 1
        self.addNode(self.LinkedList(key=key, val=value))
        self.m[key] = self.head.next
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity =capacity
#         self.dict = OrderedDict()

#     def get(self, key: int) -> int:
#         if key in self.dict.keys():
#             res = self.dict[key]
#             self.dict.move_to_end(key, last=True)
#             return res
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.dict.keys():
#             self.dict[key]= value
#             self.dict.move_to_end(key, last=True)
#         else:
#             if self.capacity==0:
#                 self.dict.popitem(last=False)
#             else:
#                 self.capacity-=1
#             self.dict[key]= value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value