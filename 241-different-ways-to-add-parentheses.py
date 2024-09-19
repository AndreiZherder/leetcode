"""
Given a string expression of numbers and operators, return all possible results from computing
all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different
results does not exceed 104.



Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].

"""
from operator import mul, add, sub
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {'*': mul, '+': add, '-': sub}
        n = len(expression)
        if n == 0:
            return []
        if n == 1:
            return [int(expression)]
        if n == 2 and expression[0].isdigit():
            return [int(expression)]
        ans = []
        for i, c in enumerate(expression):
            if not c.isdigit():
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        ans.append(ops[c](l, r))
        return ans


def main():
    expression = "2*3-4*5"
    print(Solution().diffWaysToCompute(expression))


if __name__ == '__main__':
    main()
