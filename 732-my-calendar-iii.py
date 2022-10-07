"""
A k-booking happens when k events have some non-empty intersection
(i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event,
return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists
a k-booking in the calendar.


Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20);
// return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60);
// return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40);
// return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15);
// return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10);
// return 3
myCalendarThree.book(25, 55);
// return 3


Constraints:

0 <= start < end <= 109
At most 400 calls will be made to book.
"""

from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()
        self.ans = 0

    def book(self, start: int, end: int) -> int:
        left = self.d.bisect_left(start)
        right = self.d.bisect_left(end)
        for i in range(left, right):
            k, v = self.d.peekitem(i)
            self.d[k] = v + 1
            self.ans = max(self.ans, v + 1)

        if start not in self.d:
            i = self.d.bisect_left(start) - 1
            if i != -1:
                k, v = self.d.peekitem(i)
                self.d[start] = v + 1
                self.ans = max(self.ans, v + 1)
            else:
                self.d[start] = 1
                self.ans = max(self.ans, 1)
        if end not in self.d:
            i = self.d.bisect_left(end) - 1
            k, v = self.d.peekitem(i)
            self.d[end] = v - 1
        return self.ans


def main():
    myCalendarThree = MyCalendarThree()
    print(myCalendarThree.book(5, 12))
    print(myCalendarThree.book(42, 50))
    print(myCalendarThree.book(4, 9))
    print(myCalendarThree.book(33, 41))
    print(myCalendarThree.book(2, 7))
    print(myCalendarThree.book(16, 25))
    print(myCalendarThree.book(7, 16))


if __name__ == '__main__':
    main()
