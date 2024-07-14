"""
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters,
representing the name.

One or more digits representing that element's count may follow if the count is greater than 1.
If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.



Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

"""
from collections import Counter
from typing import List


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = []
        cur = Counter()
        i = 0
        while i < n:
            if formula[i] == '(':
                stack.append(cur)
                cur = Counter()
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                m = 1
                if i + 1 != j:
                    m = int(formula[i + 1:j])
                for k in cur:
                    cur[k] *= m
                cur += stack.pop()
                i = j
            else:
                if i + 1 < n and formula[i + 1].isalpha() and formula[i + 1].islower():
                    k = formula[i: i + 2]
                    i += 2
                else:
                    k = formula[i: i + 1]
                    i += 1
                j = i
                m = 1
                while j < n and formula[j].isdigit():
                    j += 1
                if j != i:
                    m = int(formula[i:j])
                    i = j
                cur[k] += m
                i = j
        ans = []
        for k, v in sorted(cur.items()):
            if v > 1:
                ans.append(f'{k}{v}')
            else:
                ans.append(f'{k}')
        return ''.join(ans)


def main():
    formula = "K4(ON(SO3)2)2"
    print(Solution().countOfAtoms(formula))


if __name__ == '__main__':
    main()
