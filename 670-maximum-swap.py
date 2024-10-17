"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints:

0 <= num <= 108

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        best = s[:]
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]
                if s > best:
                    best = s[:]
                s[i], s[j] = s[j], s[i]
        return int(''.join(best))


def main():
    num = 98800435
    print(Solution().maximumSwap(num))


if __name__ == '__main__':
    main()
