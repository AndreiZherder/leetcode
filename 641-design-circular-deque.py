"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful,
or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful,
or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful,
or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful,
or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
"deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.nums = [0 for i in range(k)]
        self.head = 0
        self.tail = k - 1
        self.k = k
        self.len = 0

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self.nums[self.head] = value
            self.head = (self.head + 1) % self.k
            return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self.nums[self.tail] = value
            self.tail = (self.tail - 1) % self.k
            return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self.head = (self.head - 1) % self.k
            return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self.tail = (self.tail + 1) % self.k
            return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        else:
            return self.nums[(self.head - 1) % self.k]

    def getRear(self) -> int:
        if self.len == 0:
            return -1
        else:
            return self.nums[(self.tail + 1) % self.k]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


def main():
    myCircularDeque = MyCircularDeque(3)
    print(myCircularDeque.insertLast(1))
    print(myCircularDeque.insertLast(2))
    print(myCircularDeque.insertFront(3))
    print(myCircularDeque.insertFront(4))
    print(myCircularDeque.getRear())
    print(myCircularDeque.isFull())
    print(myCircularDeque.deleteLast())
    print(myCircularDeque.insertFront(4))
    print(myCircularDeque.getFront())


if __name__ == '__main__':
    main()
