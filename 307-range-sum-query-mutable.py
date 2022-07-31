"""
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""
from typing import List


class Node:
    def __init__(self, num: int, left: int, right: int, parent: int, level: int):
        self.num = num
        self.left = left
        self.right = right
        self.parent = parent
        self.level = level
        self.total = 0


class NumArray:

    def __init__(self, nums: List[int]):
        def make_tree(left: int, right: int, parent: int, level: int) -> int:
            if left == right:
                self.nodes[left] = Node(nums[left], -1, -1, parent, level)
                self.nodes[left].total = nums[left]
                return self.nodes[left].total
            else:
                mid = left + (right - left) // 2
                if mid == left:
                    self.nodes[mid] = Node(nums[mid], -1, right, parent, level)
                    self.nodes[mid].total = nums[mid] + make_tree(mid + 1, right, mid, level + 1)
                    return self.nodes[mid].total
                else:
                    self.nodes[mid] = Node(nums[mid],
                                           left + (mid - 1 - left) // 2,
                                           mid + 1 + (right - mid - 1) // 2,
                                           parent,
                                           level)
                    left_total = make_tree(left, mid - 1, mid, level + 1)
                    right_total = make_tree(mid + 1, right, mid, level + 1)
                    self.nodes[mid].total = nums[mid] + left_total + right_total
                    return self.nodes[mid].total

        self.nodes = [None for i in range(len(nums))]
        make_tree(0, len(nums) - 1, -1, 0)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nodes[index].num
        self.nodes[index].num = val
        while index != -1:
            self.nodes[index].total += delta
            index = self.nodes[index].parent

    def sumRange(self, left: int, right: int) -> int:
        level_left = self.nodes[left].level
        level_right = self.nodes[right].level
        index_left = left
        index_right = right
        left_total = 0
        if self.nodes[index_left].left != -1:
            left_total = self.nodes[self.nodes[index_left].left].total
        right_total = 0
        if self.nodes[index_right].right != -1:
            right_total = self.nodes[self.nodes[index_right].right].total

        if level_left > level_right:
            min_level = level_right
            while self.nodes[index_left].level > min_level:
                if index_left < left:
                    tmp = 0
                    if self.nodes[index_left].left != -1:
                        tmp = self.nodes[self.nodes[index_left].left].total
                    left_total += self.nodes[index_left].num + tmp
                index_left = self.nodes[index_left].parent
        else:
            min_level = level_left
            while self.nodes[index_right].level > min_level:
                if index_right > right:
                    tmp = 0
                    if self.nodes[index_right].right != -1:
                        tmp = self.nodes[self.nodes[index_right].right].total
                    right_total += self.nodes[index_right].num + tmp
                index_right = self.nodes[index_right].parent

        while index_left != index_right:
            if index_left < left:
                tmp = 0
                if self.nodes[index_left].left != -1:
                    tmp = self.nodes[self.nodes[index_left].left].total
                left_total += self.nodes[index_left].num + tmp
            if index_right > right:
                tmp = 0
                if self.nodes[index_right].right != -1:
                    tmp = self.nodes[self.nodes[index_right].right].total
                right_total += self.nodes[index_right].num + tmp
            index_left = self.nodes[index_left].parent
            index_right = self.nodes[index_right].parent

        least_common_ancestor_index = index_left
        return self.nodes[least_common_ancestor_index].total - left_total - right_total


def main():
    numArray = NumArray([1, 3, 5])
    print(numArray.sumRange(0, 2))
    numArray.update(1, 2)
    print(numArray.sumRange(0, 2))


if __name__ == '__main__':
    main()
