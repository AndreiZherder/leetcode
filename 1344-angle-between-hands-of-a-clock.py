"""
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.



Example 1:
Input: hour = 12, minutes = 30
Output: 165
Example 2:
Input: hour = 3, minutes = 30
Output: 75
Example 3:
Input: hour = 3, minutes = 15
Output: 7.5


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        a1 = 360 * minutes / 60
        a2 = 360 * hour / 12 + 360 // 12 * minutes / 60
        if abs(a1 - a2) <= 180:
            return abs(a1 - a2)
        else:
            return 360 - abs(a1 - a2)


def main():
    hour = 3
    minutes = 15
    print(Solution().angleClock(hour, minutes))


if __name__ == '__main__':
    main()
