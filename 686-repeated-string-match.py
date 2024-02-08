"""
Given two strings a and b, return the minimum number of times you should repeat string a so that string b
is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".



Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2


Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.

"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        if b in a:
            return 1
        if b in 2 * a:
            return 2
        i = b.find(a)
        if i == -1:
            return -1
        ans = 1
        k = 0
        for j in range(i + n, m):
            if b[j] != a[k % n]:
                return -1
            k += 1
        ans += (m - i - n + n - 1) // n
        k = n - 1
        for j in range(i - 1, -1, -1):
            if b[j] != a[k % n]:
                return -1
            k -= 1
        ans += (i + n - 1) // n
        return ans



def main():
    a = "abcd"
    b = "cdabcdab"
    print(Solution().repeatedStringMatch(a, b))


if __name__ == '__main__':
    main()
