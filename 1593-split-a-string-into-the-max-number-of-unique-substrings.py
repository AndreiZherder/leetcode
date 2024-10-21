"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings
forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc']
is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.


Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

"""
from typing import Set


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(i: int, cur: Set[str], last_word: str):
            if i == n:
                if not last_word:
                    ans[0] = max(ans[0], len(cur))
            else:
                new_word = last_word + s[i]
                if new_word not in cur:
                    cur.add(new_word)
                    backtrack(i + 1, cur, '')
                    cur.remove(new_word)
                backtrack(i + 1, cur, new_word)
        n = len(s)
        ans = [0]
        backtrack(0, set(), '')
        return ans[0]


def main():
    s = "ababccc"
    print(Solution().maxUniqueSplit(s))


if __name__ == '__main__':
    main()
