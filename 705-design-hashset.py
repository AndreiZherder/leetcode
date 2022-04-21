"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""


class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next


class MyHashSet:
    def __init__(self):
        self.m = 16384
        self.hashmap = [None for i in range(self.m)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            if self.hashmap[key % self.m]:
                next = self.hashmap[key % self.m]
                self.hashmap[key % self.m] = Node(key, next)
            else:
                self.hashmap[key % self.m] = Node(key)

    def remove(self, key: int) -> None:
        if self.hashmap[key % self.m]:
            node = self.hashmap[key % self.m]
            prev = None
            while node:
                if node.val == key:
                    if prev:
                        prev.next = node.next
                    else:
                        self.hashmap[key % self.m] = node.next
                    return
                else:
                    prev = node
                    node = node.next

    def contains(self, key: int) -> bool:
        if self.hashmap[key % self.m]:
            node = self.hashmap[key % self.m]
            while node:
                if node.val == key:
                    return True
                else:
                    node = node.next
        return False


def main():
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print(myHashSet.contains(1))
    print(myHashSet.contains(3))
    myHashSet.add(2)
    print(myHashSet.contains(2))
    myHashSet.remove(2)
    print(myHashSet.contains(2))


if __name__ == '__main__':
    main()
