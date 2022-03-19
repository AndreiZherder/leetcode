"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top.
The stack becomes [5,7].


Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""
from collections import Counter


class FreqStack:

    def __init__(self):
        self.counter = Counter()
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[self.counter[val] - 1].append(val)

    def pop(self) -> int:
        val = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        self.counter[val] -= 1
        return val


def main():
    freqstack = FreqStack()
    for num in [5, 7, 5, 7, 4, 5]:
        freqstack.push(num)
    while freqstack:
        print(freqstack.pop(), end=' ')


if __name__ == '__main__':
    main()
