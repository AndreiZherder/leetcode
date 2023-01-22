"""
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits,
return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

1 <= s.length <= 20
s consists of digits only.
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(i: int, left: int) -> List[List[str]]:
            if n - i < left or n - i > left * 3:
                return []
            if left == 1:
                if i == n - 1 or (int(s[i:]) <= 255 and s[i] != '0'):
                    return [[s[i:]]]
                else:
                    return []
            ans = []
            if int(s[i:i + 3]) <= 255 and s[i] != '0':
                for path in dfs(i + 3, left - 1):
                    ans.append([s[i:i + 3]] + path)
            if s[i] != '0':
                for path in dfs(i + 2, left - 1):
                    ans.append([s[i:i + 2]] + path)
            for path in dfs(i + 1, left - 1):
                ans.append([s[i:i + 1]] + path)
            return ans

        n = len(s)
        left = 4
        return ['.'.join(path) for path in dfs(0, 4)]


def main():
    s = "101023"
    print(Solution().restoreIpAddresses(s))


if __name__ == '__main__':
    main()
