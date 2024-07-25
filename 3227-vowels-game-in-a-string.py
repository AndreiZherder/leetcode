"""
Alice and Bob are playing a game on a string.

You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

On Alice's turn, she has to remove any non-empty
substring
 from s that contains an odd number of vowels.
On Bob's turn, he has to remove any non-empty
substring
 from s that contains an even number of vowels.
The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

Return true if Alice wins the game, and false otherwise.

The English vowels are: a, e, i, o, and u.



Example 1:

Input: s = "leetcoder"

Output: true

Explanation:
Alice can win the game as follows:

Alice plays first, she can delete the underlined substring in s = "leetcoder" which contains 3 vowels.
The resulting string is s = "der".
Bob plays second, he can delete the underlined substring in s = "der" which contains 0 vowels.
The resulting string is s = "er".
Alice plays third, she can delete the whole string s = "er" which contains 1 vowel.
Bob plays fourth, since the string is empty, there is no valid play for Bob. So Alice wins the game.
Example 2:

Input: s = "bbcd"

Output: false

Explanation:
There is no valid play for Alice in her first turn, so Alice loses the game.



Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.

"""
from collections import deque
from itertools import groupby


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        odd = deque()
        even = deque()
        for k, g in groupby(s):
            if k in 'aeiou':
                v = len(list(g))
                if v % 2 == 1:
                    if v != 1:
                        odd.append(v)
                    else:
                        odd.appendleft(v)
                else:
                    even.append(v)
        alice = True
        while odd or even:
            if alice:
                if even:
                    even.pop()
                    odd.appendleft(1)
                else:
                    odd.pop()
            else:
                if even:
                    even[-1] -= 2
                    if even[-1] == 0:
                        even.pop()
                else:
                    if odd[-1] != 1:
                        odd[-1] -= 2
                    else:
                        return True
            alice = not alice
        return not alice


def main():
    s = "leetcoder"
    print(Solution().doesAliceWin(s))


if __name__ == '__main__':
    main()
