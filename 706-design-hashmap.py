"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""


class Node:
    def __init__(self, key: int, value: int, next: 'Node' = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.m = 16384
        self.hashmap = [None for i in range(self.m)]

    def put(self, key: int, value: int) -> None:
        if self.hashmap[key % self.m]:
            node = self.hashmap[key % self.m]
            while node:
                if node.key == key:
                    node.value = value
                    return
                else:
                    node = node.next
            next = self.hashmap[key % self.m]
            self.hashmap[key % self.m] = Node(key, value, next)
        else:
            self.hashmap[key % self.m] = Node(key, value)

    def get(self, key: int) -> int:
        if self.hashmap[key % self.m]:
            node = self.hashmap[key % self.m]
            while node:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
        return -1

    def remove(self, key: int) -> None:
        if self.hashmap[key % self.m]:
            node = self.hashmap[key % self.m]
            prev = None
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next
                    else:
                        self.hashmap[key % self.m] = node.next
                    return
                else:
                    prev = node
                    node = node.next


def main():
    myHashMap = MyHashMap()
    print(myHashMap.put(1, 1))
    print(myHashMap.put(2, 2))
    print(myHashMap.get(1))
    print(myHashMap.get(3))
    print(myHashMap.put(2, 1))
    print(myHashMap.get(2))
    print(myHashMap.remove(2))
    print(myHashMap.get(2))


if __name__ == '__main__':
    main()
