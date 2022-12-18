"""
Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones.
Otherwise, return false.



Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
s[0] is '1'.
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        state = 1
        for c in s:

            if state == 1:
                if c == '1':
                    state = 2
                continue

            if state == 2:
                if c == '0':
                    state = 3
                continue

            if state == 3 and c == '1':
                return False

        return True


def main():
    s = "1001"
    print(Solution().checkOnesSegment(s))


if __name__ == '__main__':
    main()
