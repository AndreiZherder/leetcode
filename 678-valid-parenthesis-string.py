"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        stars = 0
        for c in s:
            if c == '*':
                stars += 1
            elif c == '(':
                cnt += 1
            elif c == ')':
                if cnt > 0:
                    cnt -= 1
                elif stars > 0:
                    stars -= 1
                else:
                    return False

        cnt = 0
        stars = 0
        for c in reversed(s):
            if c == '*':
                stars += 1
            elif c == ')':
                cnt += 1
            elif c == '(':
                if cnt > 0:
                    cnt -= 1
                elif stars > 0:
                    stars -= 1
                else:
                    return False
        return True


def main():
    s = "()))))**)(()*()**)))()*)()())*(*)())**()*)))(**())))()**))*)*()**((*(*"
    print(Solution().checkValidString(s))


if __name__ == '__main__':
    main()
