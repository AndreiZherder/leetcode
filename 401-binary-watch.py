"""
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".
Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".


Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []


Constraints:

0 <= turnedOn <= 10
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def dfs(i: int, num: int, k: int):
            if i == n or k > turnedOn:
                return
            if k == turnedOn:
                nums.append(num | (1 << i))
            dfs(i + 1, num, k)
            dfs(i + 1, num | (1 << i), k + 1)

        def bin2time(num: int) -> str:
            minutes = num & 0x3F
            if minutes > 59:
                return ''
            hours = (num & 0x3C0) >> 6
            if hours > 11:
                return ''
            minutes = '0' + str(minutes) if minutes < 10 else str(minutes)
            hours = str(hours)
            return ':'.join((hours, minutes))

        if turnedOn >= 9:
            return []
        if turnedOn == 0:
            return ['0:00']
        n = 10
        nums = []
        dfs(0, 0, 1)
        ans = []
        for num in nums:
            time = bin2time(num)
            if time:
                ans.append(time)
        return ans


def main():
    turnedOn = 1
    print(Solution().readBinaryWatch(turnedOn))


if __name__ == '__main__':
    main()
