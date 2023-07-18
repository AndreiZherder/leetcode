"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

"""


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.head_dummy = ListNode(-100)
        self.tail_dummy = ListNode(-101)
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy
        self.d = dict()

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            node.prev.next, node.next.prev = node.next, node.prev
            self.head_dummy.next.prev, node.prev, self.head_dummy.next, node.next = node, self.head_dummy, node, self.head_dummy.next
            return self.d[key].val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = (key, value)
            node.prev.next, node.next.prev = node.next, node.prev
            self.head_dummy.next.prev, node.prev, self.head_dummy.next, node.next = node, self.head_dummy, node, self.head_dummy.next
        else:
            if self.n < self.capacity:
                node = ListNode((key, value))
                self.d[key] = node
                self.head_dummy.next.prev, node.prev, self.head_dummy.next, node.next = node, self.head_dummy, node, self.head_dummy.next
                self.n += 1
            else:
                node = ListNode((key, value))
                self.d[key] = node
                self.head_dummy.next.prev, node.prev, self.head_dummy.next, node.next = node, self.head_dummy, node, self.head_dummy.next
                del self.d[self.tail_dummy.prev.val[0]]
                self.tail_dummy.prev.prev.next, self.tail_dummy.prev = self.tail_dummy, self.tail_dummy.prev.prev


def main():
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1))
    print(lRUCache.put(2, 2))
    print(lRUCache.get(1))
    print(lRUCache.put(3, 3))
    print(lRUCache.get(2))
    print(lRUCache.put(4, 4))
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))


if __name__ == '__main__':
    main()
