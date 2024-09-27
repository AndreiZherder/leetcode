"""
You are implementing a program to use as your calendar. We can add a new event
if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection
(i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
[start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing
a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked.
myCalendarTwo.book(50, 60); // return True, The event can be booked.
myCalendarTwo.book(10, 40); // return True, The event can be double booked.
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10
which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40)
will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55)
will be double booked with the second event.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.

"""
from sortedcontainers import SortedList


class MyCalendarTwo:

    def __init__(self):
        self.sl = SortedList([(-1, 0)])

    def book(self, start: int, end: int) -> bool:
        i = self.sl.bisect_right((start, 1001)) - 1
        if self.sl[i][0] == start:
            tmp = self.sl[i]
            if tmp[1] == 2:
                return False
            saved = SortedList(self.sl)
            self.sl.pop(i)
            self.sl.add((tmp[0], tmp[1] + 1))
            i += 1
        else:
            if self.sl[i][1] == 2:
                return False
            saved = SortedList(self.sl)
            self.sl.add((start, self.sl[i][1] + 1))
            i += 2
        while i < len(self.sl) and self.sl[i][0] < end:
            tmp = self.sl[i]
            if tmp[1] == 2:
                self.sl = saved
                return False
            self.sl.pop(i)
            self.sl.add((tmp[0], tmp[1] + 1))
            i += 1
        if i == len(self.sl):
            self.sl.add((end, 0))
        elif self.sl[i][0] != end:
            self.sl.add((end, self.sl[i - 1][1] - 1))
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


def main():
    myCalendarTwo = MyCalendarTwo()
    print(myCalendarTwo.book(97, 100))
    print(myCalendarTwo.book(51, 65))
    print(myCalendarTwo.book(27, 46))
    print(myCalendarTwo.book(90, 100))
    print(myCalendarTwo.book(20, 32))
    print(myCalendarTwo.book(15, 28))
    print(myCalendarTwo.book(60, 73))
    print(myCalendarTwo.book(77, 91))
    print(myCalendarTwo.book(67, 85))
    print(myCalendarTwo.book(58, 72))
    print(myCalendarTwo.book(74, 93))
    print(myCalendarTwo.book(73, 83))
    print(myCalendarTwo.book(71, 87))
    print(myCalendarTwo.book(97, 100))
    print(myCalendarTwo.book(14, 31))
    print(myCalendarTwo.book(26, 37))
    print(myCalendarTwo.book(66, 76))
    print(myCalendarTwo.book(52, 67))
    print(myCalendarTwo.book(24, 43))
    print(myCalendarTwo.book(6, 23))
    print(myCalendarTwo.book(94, 100))
    print(myCalendarTwo.book(33, 44))
    print(myCalendarTwo.book(30, 46))
    print(myCalendarTwo.book(6, 20))
    print(myCalendarTwo.book(71, 87))
    print(myCalendarTwo.book(49, 59))



if __name__ == '__main__':
    main()
