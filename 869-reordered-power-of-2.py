"""
You are given an integer n. We reorder the digits in any order (including the original order)
such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.



Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false


Constraints:

1 <= n <= 10^9
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_digits(n: int) -> List[int]:
            ans = []
            while n > 0:
                ans.append(n % 10)
                n //= 10
            return ans
        counters = defaultdict(list)
        for i in range(30):
            digits = get_digits(1 << i)
            counters[len(digits)].append(Counter(digits))
        digits = get_digits(n)
        counter1 = Counter(digits)
        return any(counter == counter1 for counter in counters[len(digits)])


def main():
    n = 125
    print(Solution().reorderedPowerOf2(n))


if __name__ == '__main__':
    main()
