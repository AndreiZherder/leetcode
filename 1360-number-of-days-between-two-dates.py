"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Constraints:

The given dates are valid dates between the years 1971 and 2100.

"""
from typing import List

from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        delta = date(*map(int, date1.split('-'))) - date(*map(int, date2.split('-')))
        return abs(delta.days)


def main():
    date1 = "2019-06-29"
    date2 = "2019-06-30"
    print(Solution().daysBetweenDates(date1, date2))


if __name__ == '__main__':
    main()
