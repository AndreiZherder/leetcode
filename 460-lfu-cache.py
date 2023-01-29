"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.
When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting
a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency),
the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3


Constraints:

0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
"""


class Header:

    def __init__(self, *, val=None, prev=None, next=None, head=None, tail=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.head = head
        self.tail = tail


class ListNode:

    def __init__(self, *, val=None, prev=None, next=None, header=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.header = header


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.header = Header(val=0)

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.cache:
            self.update(key)
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key][0] = value
            self.update(key)
        else:
            if len(self.cache) == self.capacity:
                self.invalidate()
            node = self.add_node(key, self.header)
            self.cache[key] = [value, 1, node]

    def add_node(self, key: int, header: Header) -> ListNode:
        if not header.next:
            header.next = Header(val=header.val + 1, prev=header)
            header.next.head = ListNode(val=0, header=header)
            header.next.tail = None
        if header.next.val - 1 > header.val:
            new = Header(val=header.val + 1, prev=header)
            new.head = ListNode(val=0, header=new)
            new.tail = None
            new.next = header.next
            header.next.prev = new
            header.next = new

        header = header.next
        if not header.tail:
            header.head.next = ListNode(val=key, prev=header.head, header=header)
            header.tail = header.head.next
        else:
            header.tail.next = ListNode(val=key, prev=header.tail, header=header)
            header.tail = header.tail.next
        return header.tail

    def invalidate(self):
        header = self.header.next
        del self.cache[header.head.next.val]
        header.head.next = header.head.next.next
        if not header.head.next:
            if header.next:
                header.next.prev = header.prev
            header.prev.next = header.next
        else:
            header.head.next.prev = header.head

    def update(self, key):
        value, freq, node = self.cache[key]
        header = node.header
        self.cache[key] = [value, freq + 1, self.add_node(key, header)]
        if node.next:
            node.next.prev = node.prev
        node.prev.next = node.next
        if not header.head.next:
            if header.next:
                header.next.prev = header.prev
            header.prev.next = header.next
            return
        if node == header.tail:
            header.tail = node.prev


def main():
    # ["LFUCache", "put", "put", "put", "put", "get"]
    # [[2], [3, 1], [2, 1], [2, 2], [4, 4], [2]]

    # lfu = LFUCache(2)
    # print(lfu.put(3, 1))
    # print(lfu.put(2, 1))
    # print(lfu.put(2, 2))
    # print(lfu.put(4, 4))
    # print(lfu.get(2))

    # ["LFUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
    # [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]
    lfu = LFUCache(3)
    print(lfu.put(1, 1))
    print(lfu.put(2, 2))
    print(lfu.put(3, 3))
    print(lfu.put(4, 4))
    print(lfu.get(4))
    print(lfu.get(3))
    print(lfu.get(2))
    print(lfu.get(1))
    print(lfu.put(5, 5))
    print(lfu.get(1))
    print(lfu.get(2))
    print(lfu.get(3))
    print(lfu.get(4))
    print(lfu.get(5))


if __name__ == '__main__':
    main()
