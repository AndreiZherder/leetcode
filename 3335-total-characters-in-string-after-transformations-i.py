"""
You are given a string s and an integer t, representing the number of transformations to perform.
In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet.
For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.


Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105

"""
from collections import Counter
from string import ascii_lowercase
from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        counter = [0 for i in range(26)]
        for c in s:
            counter[ord(c) - ord('a')] += 1
        while t:
            tmp = 0
            for c in reversed(ascii_lowercase):
                if c == 'z':
                    tmp = counter[25]
                    counter[25] = 0
                else:
                    i = ord(c) - ord('a')
                    counter[i + 1] += counter[i]
                    counter[i] = 0
            counter[0] += tmp
            counter[1] += tmp
            t -= 1
        return sum(counter) % mod


def main():
    s = "z"
    t = 27
    print(Solution().lengthAfterTransformations(s, t))


if __name__ == '__main__':
    main()
